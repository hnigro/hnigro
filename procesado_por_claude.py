"""
SRT Manager - A tool for managing SRT devices and integrating with ARYA system.

This module provides functionality to manage SRT devices, generate CSV files
containing route information, and upload them to the ARYA system through
a Swagger API.

Author: [Your Name]
Last Updated: 2025-04-23
"""

import os
import json
import time
import logging
import datetime
import requests
import configparser
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Suppress insecure request warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("srt_manager.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("SRTManager")

# Constants
CONFIG_FILE = "config.ini"
CSV_DIRECTORY = "CSV_FILES"
DEFAULT_TIMEOUT = 30  # seconds


@dataclass
class SRTDevice:
    """
    Data class representing an SRT device with its connection details.
    """
    name: str
    ip_address: str
    username: str
    password: str
    description: str = ""

    def __str__(self) -> str:
        return f"{self.name} ({self.ip_address})"


class ConfigManager:
    """
    Manages configuration settings for the application.
    Handles loading device configurations from file or environment variables.
    """

    def __init__(self, config_file: str = CONFIG_FILE):
        """Initialize the ConfigManager with a configuration file."""
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self._load_config()

    def _load_config(self) -> None:
        """Load configuration from file or create a default one if not exists."""
        config_path = Path(self.config_file)

        if config_path.exists():
            logger.info(f"Loading configuration from {self.config_file}")
            self.config.read(self.config_file)
        else:
            logger.warning(f"Configuration file {self.config_file} not found. Creating default.")
            self._create_default_config()

    def _create_default_config(self) -> None:
        """Create a default configuration file."""
        self.config["SWAGGER"] = {
            "url": "http://10.133.96.78:8081/api/v1",
            "client_id": "SRT",
            "client_secret": "srtapi"
        }

        self.config["GENERAL"] = {
            "csv_directory": CSV_DIRECTORY,
            "refresh_interval": "60"  # seconds
        }

        # Write the default config to file
        with open(self.config_file, 'w') as config_file:
            self.config.write(config_file)

    def get_swagger_config(self) -> Dict[str, str]:
        """Get Swagger API configuration."""
        return dict(self.config["SWAGGER"])

    def get_devices(self) -> List[SRTDevice]:
        """
        Get all configured SRT devices.

        Returns:
            List[SRTDevice]: List of configured SRT devices
        """
        devices = []

        # First check for devices in config file
        for section in self.config.sections():
            if section.startswith("DEVICE_"):
                device_config = self.config[section]
                devices.append(
                    SRTDevice(
                        name=device_config.get("name", section),
                        ip_address=device_config.get("ip_address", ""),
                        username=device_config.get("username", ""),
                        password=device_config.get("password", ""),
                        description=device_config.get("description", "")
                    )
                )

        # If no devices in config, use the default hardcoded list
        # In a production environment, this should be removed and proper configuration enforced
        if not devices:
            logger.warning("No devices found in config, using default device list")
            devices = self._get_default_devices()

        return devices

    def _get_default_devices(self) -> List[SRTDevice]:
        """
        Get default hardcoded list of devices.
        This is included for backward compatibility and should be removed in production.
        """
        # Note: In a production environment, credentials should never be hardcoded
        # This is only included for compatibility with the original code
        return [
            SRTDevice("SRT-ABC-01", "10.177.58.101", "haiadmin", "tnstafl2420", "SRT-ABC-01"),
            SRTDevice("SRT-ABC-02", "172.22.99.102", "haiadmin", "tnstafl2420", "SRT-ABC-02"),
            SRTDevice("SRT-ABC-03", "10.177.58.103", "haiadmin", "tnstafl2420", "SRT-ABC-03"),
            SRTDevice("SRT-ABC-04", "172.22.99.104", "haiadmin", "tnstafl2420", "SRT-ABC-04"),
            SRTDevice("SRT-ABC-05", "10.177.58.105", "haiadmin", "tnstafl2420", "SRT-ABC-05"),
            SRTDevice("SRT-CBC-01", "10.133.92.150", "haiadmin", "tnstafl2420", "SRT-CBC-01"),
            SRTDevice("SRT-CBC-02", "172.23.241.150", "haiadmin", "tnstafl2420", "SRT-CBC-02"),
            # Add the rest of the devices here
        ]

    def get_refresh_interval(self) -> int:
        """Get the refresh interval in seconds."""
        try:
            return int(self.config.get("GENERAL", "refresh_interval", fallback="60"))
        except ValueError:
            logger.warning("Invalid refresh interval in config, using default of 60 seconds")
            return 60


class SwaggerAPI:
    """
    Handles interactions with the Swagger API for data upload.
    """

    def __init__(self, config: Dict[str, str]):
        """
        Initialize the SwaggerAPI with configuration.

        Args:
            config: Dictionary containing Swagger API configuration
        """
        self.base_url = config.get("url", "http://10.133.96.78:8081/api/v1")
        self.client_id = config.get("client_id", "SRT")
        self.client_secret = config.get("client_secret", "srtapi")

        # Set environment variable for OAuth insecure transport (development only)
        # In production, secure connections should be used
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    def upload_csv(self, csv_path: str) -> bool:
        """
        Upload a CSV file to the Swagger API.

        Args:
            csv_path: Path to the CSV file to upload

        Returns:
            bool: True if upload was successful, False otherwise
        """
        try:
            # Create OAuth client
            client = BackendApplicationClient(client_id=self.client_id)
            oauth = OAuth2Session(client=client)

            # Get token
            token_url = f"{self.base_url}/login"
            token = oauth.fetch_token(
                token_url=token_url,
                client_id=self.client_id,
                client_secret=self.client_secret
            )

            if not token:
                logger.error("Failed to obtain OAuth token")
                return False

            # Prepare file for upload
            with open(csv_path, "rb") as file:
                csv_file = {"file": (os.path.basename(csv_path), file, "application/vnd.ms-excel")}

                # Upload file
                swagger_cmd = f"{self.base_url}/ingest/classes/SRT/entry/csv?overrideValidation=true&hasHeaderRow=true&insertOnly=false&verbose=low&uniqueIdColumns=0"
                response = oauth.post(url=swagger_cmd, files=csv_file)

                if response.status_code in (200, 201, 202):
                    logger.info(f"Successfully uploaded {csv_path} to Swagger API")
                    return True
                else:
                    logger.error(
                        f"Failed to upload {csv_path}. Status code: {response.status_code}, Response: {response.text}")
                    return False

        except Exception as e:
            logger.exception(f"Error uploading CSV file: {str(e)}")
            return False


class SRTManager:
    """
    Manages SRT devices, retrieves route information and generates CSV files.
    """

    def __init__(self, device: SRTDevice, csv_directory: str = CSV_DIRECTORY):
        """
        Initialize the SRTManager with a device.

        Args:
            device: SRT device to manage
            csv_directory: Directory to store generated CSV files
        """
        self.device = device
        self.csv_directory = csv_directory
        self.session = requests.Session()
        self._ensure_csv_directory()

    def _ensure_csv_directory(self) -> None:
        """Ensure the CSV directory exists."""
        os.makedirs(self.csv_directory, exist_ok=True)

    def _get_csv_path(self) -> str:
        """Get the path for the CSV file."""
        return os.path.join(self.csv_directory, f"{self.device.name}.csv")

    def _get_config_path(self) -> str:
        """Get the path for the configuration file."""
        return os.path.join(self.csv_directory, f"{self.device.name}_CONFIG.txt")

    def connect(self) -> bool:
        """
        Connect to the SRT device.

        Returns:
            bool: True if connection was successful, False otherwise
        """
        try:
            response = self.session.post(
                f"https://{self.device.ip_address}/api/session",
                json={
                    "username": self.device.username,
                    "password": self.device.password
                },
                verify=False,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code != 200:
                logger.error(f"Failed to connect to {self.device.name}. Status code: {response.status_code}")
                return False

            logger.info(f"Successfully connected to {self.device.name}")
            return True

        except Exception as e:
            logger.exception(f"Error connecting to {self.device.name}: {str(e)}")
            return False

    def get_device_id(self) -> Optional[str]:
        """
        Get the device ID.

        Returns:
            Optional[str]: Device ID if successful, None otherwise
        """
        try:
            response = self.session.get(
                f"https://{self.device.ip_address}/api/devices",
                verify=False,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code != 200:
                logger.error(f"Failed to get device ID for {self.device.name}. Status code: {response.status_code}")
                return None

            # Parse response to get device ID
            raw_data = response.text
            if raw_data.startswith("[") and raw_data.endswith("]"):
                device_data = json.loads(raw_data[1:-1])
                device_id = device_data.get("_id")
                if device_id:
                    logger.debug(f"Device ID for {self.device.name}: {device_id}")
                    return device_id

            logger.error(f"Could not parse device ID from response for {self.device.name}")
            return None

        except Exception as e:
            logger.exception(f"Error getting device ID for {self.device.name}: {str(e)}")
            return None

    def get_routes(self, device_id: str) -> Tuple[Optional[List[Dict]], Optional[str], Optional[str]]:
        """
        Get routes from the SRT device.

        Args:
            device_id: Device ID

        Returns:
            Tuple containing:
            - List of routes if successful, None otherwise
            - Input bandwidth if successful, None otherwise
            - Output bandwidth if successful, None otherwise
        """
        try:
            # Get routes
            routes_response = self.session.get(
                f"https://{self.device.ip_address}/api/gateway/{device_id}/routes?page=1&pageSize=300",
                verify=False,
                timeout=DEFAULT_TIMEOUT
            )

            if routes_response.status_code != 200:
                logger.error(f"Failed to get routes for {self.device.name}. Status code: {routes_response.status_code}")
                return None, None, None

            routes_data = json.loads(routes_response.text)

            # Get system metrics
            metrics_response = self.session.get(
                f"https://{self.device.ip_address}/api/system/metric/snapshot",
                verify=False,
                timeout=DEFAULT_TIMEOUT
            )

            if metrics_response.status_code != 200:
                logger.error(
                    f"Failed to get metrics for {self.device.name}. Status code: {metrics_response.status_code}")
                return routes_data.get("data"), None, None

            metrics_data = json.loads(metrics_response.text)
            bw_in = metrics_data.get("network", {}).get("receivedMbps")
            bw_out = metrics_data.get("network", {}).get("sentMbps")

            logger.info(f"Retrieved {len(routes_data.get('data', []))} routes from {self.device.name}")
            logger.info(f"Bandwidth for {self.device.name}: In={bw_in} Mbps, Out={bw_out} Mbps")

            return routes_data.get("data"), bw_in, bw_out

        except Exception as e:
            logger.exception(f"Error getting routes for {self.device.name}: {str(e)}")
            return None, None, None

    def generate_csv(self) -> bool:
        """
        Generate a CSV file containing route information from the SRT device.

        Returns:
            bool: True if CSV generation was successful, False otherwise
        """
        try:
            if not self.connect():
                return False

            device_id = self.get_device_id()
            if not device_id:
                return False

            routes, bw_in, bw_out = self.get_routes(device_id)
            if not routes:
                return False

            # Write routes to CSV file
            csv_path = self._get_csv_path()
            config_path = self._get_config_path()

            # Write raw data to config file for debugging
            with open(config_path, "w") as config_file:
                config_file.write(str(routes))

            # Write CSV file
            with open(csv_path, "w") as csv_file:
                # Write header
                csv_file.write(
                    "Description,Asset,Asset Type,Route Name,Source Name,Source Mode,Source Interface,"
                    "Source Address,Source Protocol,Source Port,S_SSM,Source State,Source BW,Last Update,"
                    "Destination Name,Destination Protocol,Destination Port,Destination Mode,"
                    "Destination Interface,Destination IP,Destination BW,Destination State,BW In Total,BW Out Total\n"
                )

                # Write routes
                for route in routes:
                    self._write_route_to_csv(csv_file, route, bw_in, bw_out)

            logger.info(f"Successfully generated CSV file for {self.device.name}: {csv_path}")
            return True

        except Exception as e:
            logger.exception(f"Error generating CSV for {self.device.name}: {str(e)}")
            return False

    def _write_route_to_csv(self, csv_file, route: Dict, bw_in: str, bw_out: str) -> None:
        """
        Write a route to the CSV file.

        Args:
            csv_file: Open file object for writing
            route: Route data
            bw_in: Input bandwidth
            bw_out: Output bandwidth
        """
        try:
            # Extract route information
            asset = self.device.name
            asset_type = "Broadcast"
            route_name = route.get("name", "")
            route_state = route.get("state", "")

            # Extract source information
            source = route.get("source", {})
            source_name = source.get("name", "")
            source_mode = source.get("mode", "")
            source_interface = source.get("networkInterface", "")
            source_address = source.get("address", "")
            source_protocol = source.get("protocol", "").upper()
            source_port = source.get("port", "")
            source_state = source.get("state", "")
            source_bw = source.get("usedBandwidth", "")

            # Get SSM address with fallback
            try:
                source_ssm = source.get("sourceAddress", "0.0.0.0")
            except KeyError:
                source_ssm = "0.0.0.0"

            # Get current timestamp
            last_update = datetime.datetime.now().strftime("%m/%d/%y %H:%M")

            # Generate source description
            digits = self._extract_digits_from_route_name(route_name)
            description_source = f"{asset}-{digits}-1"

            # Write source information
            csv_file.write(
                f"{description_source},{asset},{asset_type},{route_name},{source_name},{source_mode},"
                f"{source_interface},{source_address},{source_protocol},{source_port},{source_ssm},"
                f"{source_state},{source_bw},{last_update},"
            )

            # Process destinations
            destinations = route.get("destinations", [])

            # If no destinations, end the line
            if not destinations:
                csv_file.write("\n")
                return

            # Write each destination
            for i, destination in enumerate(destinations):
                dest_name = destination.get("name", "")
                dest_protocol = destination.get("protocol", "").upper()
                dest_port = destination.get("port", "")
                dest_mode = destination.get("mode", "")
                dest_interface = destination.get("networkInterface", "")
                dest_address = destination.get("address", "")
                dest_state = destination.get("state", "")

                # Get destination bandwidth with fallback
                try:
                    dest_bw = destination.get("usedBandwidth", "0")
                except KeyError:
                    dest_bw = "0"

                # For all destinations except the first, add the description prefix
                if i > 0:
                    description = f"{asset}-{digits}-{i + 1}"
                    dest_formatted_prefix = (
                        f"{description},{asset},{asset_type},{route_name},{source_name},"
                        f",,,,,,,,{last_update},"
                    )
                else:
                    dest_formatted_prefix = ""

                # Write destination information
                csv_file.write(
                    f"{dest_formatted_prefix}{dest_name},{dest_protocol},{dest_port},{dest_mode},"
                    f"{dest_interface},{dest_address},{dest_bw},{dest_state},{bw_in},{bw_out}\n"
                )

        except Exception as e:
            logger.exception(f"Error writing route to CSV: {str(e)}")

    def _extract_digits_from_route_name(self, route_name: str) -> str:
        """
        Extract digits from route name for description.

        Args:
            route_name: Route name

        Returns:
            str: Extracted digits or original route name
        """
        if len(route_name) > 3:
            if route_name[2] == "_":
                return route_name[0:2]
            elif route_name[3] == "_":
                return route_name[0:3]
        return route_name


class SRTManagerGUI:
    """
    Graphical user interface for the SRT Manager.
    """

    def __init__(self):
        """Initialize the GUI."""
        try:
            import PySimpleGUI as sg
            self.sg = sg
            self.config_manager = ConfigManager()
            self.devices = self.config_manager.get_devices()
            self.swagger_api = SwaggerAPI(self.config_manager.get_swagger_config())
            self.refresh_interval = self.config_manager.get_refresh_interval()
            self.window = None
            self.selected_device = None
            self.csv_filepath = ""
        except ImportError:
            logger.error("PySimpleGUI not installed. Run: pip install PySimpleGUI")
            raise

    def run(self) -> None:
        """Run the GUI."""
        self.sg.theme("GrayGrayGray")
        self._create_window()
        self._run_event_loop()

    def _create_window(self) -> None:
        """Create the main window."""
        # Create device list for display
        device_list = [f"{device.name} ({device.ip_address})" for device in self.devices]

        layout = [
            [self.sg.Text("SRT Manager", font=("Helvetica", 16))],
            [self.sg.Text("Select SRT device:", font=("Helvetica", 10))],
            [self.sg.Listbox(values=device_list, size=(40, 10), key="device_list", enable_events=True)],
            [self.sg.Text("", size=(40, 1), key="status_text")],
            [
                self.sg.Button("Generate CSV", key="generate_csv"),
                self.sg.Button("Upload to ARYA", key="upload_arya", disabled=True)
            ],
            [
                self.sg.Button("Update All DTH SRTs", key="update_all"),
                self.sg.Check("Auto Refresh", key="auto_refresh", enable_events=True)
            ],
            [self.sg.Button("Exit")]
        ]

        self.window = self.sg.Window(
            "SRT Manager",
            layout,
            resizable=True,
            element_justification="center",
            finalize=True
        )

    def _run_event_loop(self) -> None:
        """Run the main event loop."""
        auto_refresh_active = False
        last_refresh_time = 0

        while True:
            # Handle auto-refresh
            if auto_refresh_active and time.time() - last_refresh_time > self.refresh_interval:
                self._update_all_dth_srts()
                last_refresh_time = time.time()

            # Read window events with timeout for auto-refresh
            event, values = self.window.read(timeout=1000)

            if event in (self.sg.WIN_CLOSED, "Exit", None):
                break

            elif event == "device_list" and values["device_list"]:
                # Get selected device
                selected_device_str = values["device_list"][0]
                for device in self.devices:
                    if device.name in selected_device_str:
                        self.selected_device = device
                        break

            elif event == "generate_csv":
                if self.selected_device:
                    self._generate_csv_for_device(self.selected_device)
                else:
                    self.sg.popup("Please select a device first")

            elif event == "upload_arya":
                if self.csv_filepath:
                    self._upload_csv_to_arya(self.csv_filepath)
                else:
                    self.sg.popup("No CSV file generated yet")

            elif event == "update_all":
                self._update_all_dth_srts()

            elif event == "auto_refresh":
                auto_refresh_active = values["auto_refresh"]
                if auto_refresh_active:
                    last_refresh_time = time.time()
                    self.window["status_text"].update(f"Auto refresh enabled ({self.refresh_interval} seconds)")
                else:
                    self.window["status_text"].update("")

        self.window.close()

    def _generate_csv_for_device(self, device: SRTDevice) -> None:
        """
        Generate CSV for a specific device.

        Args:
            device: SRT device
        """
        self.window["status_text"].update(f"Generating CSV for {device.name}...")
        self.window.refresh()

        srt_manager = SRTManager(device)
        success = srt_manager.generate_csv()

        if success:
            self.csv_filepath = srt_manager._get_csv_path()
            self.window["status_text"].update(f"CSV generated: {os.path.basename(self.csv_filepath)}")
            self.window["upload_arya"].update(disabled=False)
        else:
            self.window["status_text"].update(f"Failed to generate CSV for {device.name}")

    def _upload_csv_to_arya(self, csv_path: str) -> None:
        """
        Upload CSV to ARYA.

        Args:
            csv_path: Path to CSV file
        """
        self.window["status_text"].update(f"Uploading {os.path.basename(csv_path)} to ARYA...")
        self.window.refresh()

        success = self.swagger_api.upload_csv(csv_path)

        if success:
            self.window["status_text"].update(f"Successfully uploaded to ARYA")
        else:
            self.window["status_text"].update(f"Failed to upload to ARYA")

    def _update_all_dth_srts(self) -> None:
        """Update all DTH SRTs."""
        # Filter for DTH SRTs only
        dth_devices = [device for device in self.devices if any(x in device.name for x in ["ABC", "CBC"])]

        self.window["status_text"].update(f"Updating all DTH SRTs ({len(dth_devices)} devices)...")
        self.window.refresh()

        success_count = 0

        for device in dth_devices:
            try:
                srt_manager = SRTManager(device)
                if srt_manager.generate_csv():
                    csv_path = srt_manager._get_csv_path()
                    if self.swagger_api.upload_csv(csv_path):
                        success_count += 1
            except Exception as e:
                logger.exception(f"Error updating {device.name}: {str(e)}")

        self.window["status_text"].update(f"Updated {success_count}/{len(dth_devices)} DTH SRTs")


def main() -> None:
    """Main entry point for the application."""
    try:
        # Check if running in GUI mode or command line mode
        import sys

        if len(sys.argv) > 1 and sys.argv[1] == "--cli":
            # Command line mode
            logger.info("Running in command line mode")
            config_manager = ConfigManager()
            devices = config_manager.get_devices()
            swagger_api = SwaggerAPI(config_manager.get_swagger_config())

            # Process all devices if specified
            if len(sys.argv) > 2 and sys.argv[2] == "--all":
                for device in devices:
                    try:
                        logger.info(f"Processing device: {device.name}")
                        srt_manager = SRTManager(device)
                        if srt_manager.generate_csv():
                            csv_path = srt_manager._get_csv_path()
                            swagger_api.upload_csv(csv_path)
                    except Exception as e:
                        logger.exception(f"Error processing {device.name}: {str(e)}")

            # Process specific device if specified
            elif len(sys.argv) > 2:
                device_name = sys.argv[2]
                for device in devices:
                    if device.name == device_name:
                        logger.info(f"Processing device: {device.name}")
                        srt_manager = SRTManager(device)
                        if srt_manager.generate_csv():
                            csv_path = srt_manager._get_csv_path()
                            swagger_api.upload_csv(csv_path)
                        break
                else:
                    logger.error(f"Device not found: {device_name}")

            else:
                logger.error("No device specified. Use --all to process all devices or specify a device name.")

        else:
            # GUI mode
            logger.info("Running in GUI mode")
            gui = SRTManagerGUI()
            gui.run()

    except Exception as e:
        logger.exception(f"Unhandled exception in main: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    main()