from flask import Flask, render_template, request, jsonify
import ffmpeg
import threading
import uuid
import time
from datetime import datetime

app = Flask(__name__)
active_streams = {}


class StreamManager:
    def __init__(self, stream_id, config):
        self.id = stream_id
        self.config = config
        self.process = None
        self.status = 'stopped'
        self.start_time = None
        self.logs = []

    def build_input_url(self):
        protocol = self.config['input_protocol']
        host = self.config['input_host']
        port = self.config['input_port']

        if protocol == 'srt':
            mode = self.config.get('srt_mode', 'listener')
            return f"srt://{host}:{port}?mode={mode}"
        return f"{protocol}://{host}:{port}"

    def build_output_url(self):
        protocol = self.config['output_protocol']
        host = self.config['output_host']
        port = self.config['output_port']

        if protocol == 'srt':
            mode = self.config.get('srt_output_mode', 'caller')
            return f"srt://{host}:{port}?mode={mode}"
        return f"{protocol}://{host}:{port}"

    def start(self):
        try:
            input_url = self.build_input_url()
            output_url = self.build_output_url()

            stream = ffmpeg.input(input_url)
            stream = ffmpeg.output(stream, output_url, vcodec='copy', acodec='copy', f='mpegts')

            self.process = ffmpeg.run_async(stream, pipe_stderr=True)
            self.status = 'running'
            self.start_time = datetime.now()
            self.add_log(f"Stream iniciado: {input_url} -> {output_url}")

            # Monitor en hilo separado
            threading.Thread(target=self._monitor, daemon=True).start()
            return True
        except Exception as e:
            self.add_log(f"Error: {str(e)}")
            self.status = 'error'
            return False

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process = None
            self.status = 'stopped'
            self.add_log("Stream detenido")

    def _monitor(self):
        if self.process:
            for line in iter(self.process.stderr.readline, b''):
                if line:
                    log_entry = line.decode('utf-8').strip()
                    self.add_log(log_entry)
                    if len(self.logs) > 50:  # Limitar logs
                        self.logs = self.logs[-30:]

    def add_log(self, message):
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.logs.append(f"[{timestamp}] {message}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_stream', methods=['POST'])
def create_stream():
    config = request.json
    stream_id = str(uuid.uuid4())[:8]

    stream_manager = StreamManager(stream_id, config)
    active_streams[stream_id] = stream_manager

    return jsonify({
        'status': 'success',
        'stream_id': stream_id,
        'message': 'Stream creado'
    })


@app.route('/start_stream/<stream_id>', methods=['POST'])
def start_stream(stream_id):
    if stream_id in active_streams:
        success = active_streams[stream_id].start()
        return jsonify({
            'status': 'success' if success else 'error',
            'message': 'Stream iniciado' if success else 'Error al iniciar'
        })
    return jsonify({'status': 'error', 'message': 'Stream no encontrado'})


@app.route('/stop_stream/<stream_id>', methods=['POST'])
def stop_stream(stream_id):
    if stream_id in active_streams:
        active_streams[stream_id].stop()
        return jsonify({'status': 'success', 'message': 'Stream detenido'})
    return jsonify({'status': 'error', 'message': 'Stream no encontrado'})


@app.route('/delete_stream/<stream_id>', methods=['DELETE'])
def delete_stream(stream_id):
    if stream_id in active_streams:
        active_streams[stream_id].stop()
        del active_streams[stream_id]
        return jsonify({'status': 'success', 'message': 'Stream eliminado'})
    return jsonify({'status': 'error', 'message': 'Stream no encontrado'})


@app.route('/streams_status')
def streams_status():
    streams_data = {}
    for stream_id, stream in active_streams.items():
        uptime = ''
        if stream.start_time and stream.status == 'running':
            uptime = str(datetime.now() - stream.start_time).split('.')[0]

        streams_data[stream_id] = {
            'config': stream.config,
            'status': stream.status,
            'uptime': uptime,
            'logs': stream.logs[-10:],  # Últimos 10 logs
            'input_url': stream.build_input_url(),
            'output_url': stream.build_output_url()
        }

    return jsonify(streams_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)