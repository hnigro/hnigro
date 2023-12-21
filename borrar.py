
"""
 DEFINICION DE TODOS LOS OBJECT MODEL DE LOS SRTS

[{'name': '01_ABC3_COBC1_TEST'
, 'elapsedTime': '4042:19:53'
, 'id': 'aba454e5-a2d5-4f2f-a82e-2fda732e796b'
, 'label': '284cc369-11bf-d856-f13a-58b32fc5e352'
, 'state': 'idle'
, 'source': {'name': 'h1', 'id': '22a819ab-ee3b-4a6e-8392-5f3ab2ca9612', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.77.17.170', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.170', 'encryption': 'none', 'usedBandwidth': '0.0', 'state': 'disconnected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped'}
, 'destinations': [{'name': 'COBC1', 'id': 'ab4b971b-f940-48a3-9cf6-43c02bdd7404', 'protocol': 'srt', 'port': 14056, 'started': False, 'mode': 'caller', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '191.102.238.101', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'disconnected', 'srtEncryption': 'None', 'srtLatency': 1002, 'srtOverhead': '25', 'srtPassPhrase': '', 'retainHeader': False, 'srtGroupMode': 'none', 'useFec': False, 'usedBandwidth': '0.0', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped'}]
, 'summaryStatusCode': 'unknown'
, 'summaryStatusDetails': 'idle'}

, {'name': '02_Test Haivision Canada'
, 'elapsedTime': '4919:25:47'
, 'id': 'b253ec0c-7f61-408f-8dc9-3b509294ffbd'
, 'label': '6568b65c-fba1-96b6-dc2d-6d8364faba3d'
, 'state': 'running', 'source': {'name': 'Makito X1 Canada', 'id': '7e066bac-5b97-45cf-a17e-1fc0bbd12546', 'networkInterface': 'ens33', 'mode': 'listener', 'address': '0.0.0.0', 'protocol': 'srt', 'port': 10003, 'encryption': 'none', 'usedBandwidth': '0.0', 'state': 'connecting', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'warn', 'summaryStatusDetails': 'connecting'}, 'destinations': [{'name': '02_Test Haivision Canada', 'id': '62ffa83d-16de-44fc-9aba-e1bc810a6224', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.2', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'disconnected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '0.000', 'summaryStatusCode': 'warn', 'summaryStatusDetails': 'disconnected from stream 238.77.24.2', 'shaping': True, 'maxBitrate': 10000}], 'summaryStatusCode': 'warn', 'summaryStatusDetails': 'Source Makito X1 Canada connecting'}, {'name': '04_ABC_INTER-TV_DTV-SPORTS-2_P', 'elapsedTime': '3839:39:21', 'id': '9011d5de-e145-4bee-a71a-c67142ca7832', 'label': 'e6a50430-a076-ab59-215d-5e1aded77bf7', 'state': 'running', 'source': {'name': 'DTV-SPORTS-2', 'id': '197a02d6-6711-4065-8e9f-738352aa542c', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '238.77.1.107', 'protocol': 'udp', 'port': 10000, 'sourceAddress': '10.77.22.197', 'encryption': 'none', 'usedBandwidth': '15.818', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'INTER-TV', 'id': '82444aef-9d06-4db6-a8cc-2ef7836023df', 'protocol': 'srt', 'port': 10037, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 2000, 'srtConnectionLimit': 5, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 2, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '15.818', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '05_ABC_INTER-TV_DTV-SPORTS-PLUS_P', 'elapsedTime': '3817:24:45', 'id': '1cf31869-5b98-45d7-81d5-58f0cca78bf1', 'label': 'a6cfa143-4c4c-efd3-54d9-08827eec2b7c', 'state': 'running', 'source': {'name': 'DTVSPORTS-PLUS', 'id': '79a99e00-7ca8-4dd5-9811-7e828769dc8c', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '238.77.1.108', 'protocol': 'udp', 'port': 10000, 'sourceAddress': '10.77.22.197', 'encryption': 'none', 'usedBandwidth': '15.819', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'INTER-TV', 'id': 'f46528b8-6df7-4a53-a753-579f975e5cdc', 'protocol': 'srt', 'port': 10038, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 2000, 'srtConnectionLimit': 5, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 2, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '15.818', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '06_ABC_INTER-TV_DTV-SPORTS-PAN_P', 'elapsedTime': '3839:37:20', 'id': 'cfb1912f-39a3-4fa0-bac6-312fa3a58150', 'label': '1eed7072-0ddc-b6f0-5822-5521ebabf166', 'state': 'running', 'source': {'name': 'DTV-SPORTS-PAN', 'id': 'e3c59b7e-fe9b-4ad5-98de-dec888eed440', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '238.77.1.104', 'protocol': 'udp', 'port': 10000, 'sourceAddress': '10.77.22.197', 'encryption': 'none', 'usedBandwidth': '15.816', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'INTER-TV', 'id': '120bb2c4-dd74-4f12-b0b0-70c3a463888a', 'protocol': 'srt', 'port': 10039, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 2000, 'srtConnectionLimit': 5, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 2, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '15.828', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '11_LaRed-Chile-B_ABC', 'elapsedTime': '00:00:33', 'id': '781612a7-06fe-449d-a7b3-85d47fb97e1d', 'label': 'bea0b4de-e60e-96e0-0cc6-7b8bea3e02ca', 'state': 'idle', 'source': {'name': 'LaRed-Chile-B', 'id': '52990479-4e52-4870-b59e-225ad70806cf', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '200.68.48.203', 'protocol': 'srt', 'port': 9005, 'encryption': 'srt', 'usedBandwidth': '0.0', 'state': 'disconnected', 'srtLatency': 1000, 'srtRcvBuf': 20240000, 'useFec': False, 'srtPassPhrase': 'directv2420', 'srtGroupMode': 'none', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped'}, 'destinations': [{'name': 'RCV-ABC-1209-B', 'id': 'a5d100b0-7258-468d-a75a-47c932d1a655', 'protocol': 'udp', 'port': 10000, 'started': False, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.11', 'ttl': 64, 'mtu': 1496, 'tos': 128, 'state': 'disconnected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '0.0', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'idle'}, {'name': '31_Campo_Rural_TV_ABC_B', 'elapsedTime': '1320:24:45', 'id': 'ca0240c3-8bb5-44ce-ae6e-d35aa2d63c81', 'label': '92f0b837-0ea2-413a-fe22-8e22372f451a', 'state': 'running', 'source': {'name': 'Campo Rural TV ABC B', 'id': '0c30c14d-0da8-49a7-8938-78a382ab5dcd', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '201.217.149.66', 'protocol': 'srt', 'port': 10028, 'encryption': 'none', 'usedBandwidth': '10.652', 'state': 'connected', 'srtLatency': 6000, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'RCV1274B', 'id': '7a80aaff-56ad-48e2-9a8a-ec76fe227967', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.31', 'ttl': 64, 'mtu': 1496, 'tos': 128, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '10.643', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': True, 'maxBitrate': 15000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '40_TELETUYA_GOLDDATA_ABC', 'elapsedTime': '1344:07:56', 'id': 'e3530418-f8de-4033-be38-ed9e47ebff68', 'label': '93fc3d93-30e4-9ad1-ae7f-f7245664ba10', 'state': 'running', 'source': {'name': 'TLT-GOLDDATA', 'id': '7f14c813-c9eb-4b2a-9c79-264431064ac0', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '10.202.30.1', 'protocol': 'srt', 'port': 10040, 'encryption': 'none', 'usedBandwidth': '6.645', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'VOS', 'id': '409e8480-337b-4f09-afc4-40f6a4999b77', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.40', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '6.619', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '41_ABC04_CBC02_MTV00_B_TEST', 'elapsedTime': '2644:49:34', 'id': 'f81e690b-7a90-49ba-a4d9-b8312f71477f', 'label': '49bc62a3-f6e2-a9e9-5df5-ebf888c94120', 'state': 'running', 'source': {'name': 'RCV1356_MTV00_B', 'id': '32b3f922-ae9c-4990-bb5c-28a1bd9fe342', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.77.17.164', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.164', 'encryption': 'none', 'usedBandwidth': '20.429', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC02_MTV00', 'id': 'fd06d0b8-1bcb-4adf-9895-1f860078243a', 'protocol': 'srt', 'port': 10020, 'started': True, 'mode': 'caller', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '99.193.236.205', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'None', 'srtLatency': 1000, 'srtOverhead': '25', 'srtPassPhrase': '', 'retainHeader': False, 'srtGroupMode': 'none', 'useFec': False, 'usedBandwidth': '20.429', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '42_ABC04_CBC02_TeenNick_B_TEST', 'elapsedTime': '2644:41:31', 'id': '550ebe6f-1a8c-4af8-98c8-e05e88ce430c', 'label': '18948d98-c10f-64eb-dced-63a099031fba', 'state': 'running', 'source': {'name': 'rcv1354_TeenNick_B', 'id': '2da7d492-9656-4bb8-b9bf-f229222c2ff1', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.77.17.162', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.162', 'encryption': 'none', 'usedBandwidth': '15.324', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC02-Teen Nick', 'id': 'c5bdb076-1fe8-4734-832e-aa32d94938f9', 'protocol': 'srt', 'port': 10021, 'started': True, 'mode': 'caller', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '99.193.236.205', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'None', 'srtLatency': 1000, 'srtOverhead': '25', 'srtPassPhrase': '', 'retainHeader': False, 'srtGroupMode': 'none', 'useFec': False, 'usedBandwidth': '15.324', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '51_ABC_CBC_U-1574-UNCE_P ', 'elapsedTime': '5711:57:37', 'id': 'd34cd9d2-e9c9-4bbe-a20a-d5fe6be00137', 'label': 'ac6db064-f459-a4fd-6e1b-9d0dd4780a22', 'state': 'running', 'source': {'name': 'CRIME ESTE', 'id': '09a6c3f6-fdf8-4062-8f83-184ec78ab525', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.82.17.35', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.35', 'encryption': 'none', 'usedBandwidth': '10.216', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC-01', 'id': '516375ed-0571-4b4e-ac71-d72646b00e91', 'protocol': 'srt', 'port': 10051, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 1000, 'srtConnectionLimit': 0, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 1, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '10.216', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '52_ABC_CBC_U-1575-UNRE_B', 'elapsedTime': '5711:56:47', 'id': '7350f3b1-364b-4390-a54a-1217bf17eab3', 'label': '6da4723a-afb4-9355-3204-09267b29fbf5', 'state': 'running', 'source': {'name': 'REALITY', 'id': '092764e0-2e59-4849-a1a3-17cbd3de453c', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.80.17.35', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.35', 'encryption': 'none', 'usedBandwidth': '10.216', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC-02', 'id': '606dfba9-79e8-439f-9315-8cf9688de291', 'protocol': 'srt', 'port': 10052, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 1000, 'srtConnectionLimit': 0, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 1, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '10.216', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '53_ABC_CBC_U-1576-UPRO_P ', 'elapsedTime': '818:35:14', 'id': '28e9abe8-80cb-469c-8baf-b76717ec26ee', 'label': 'f4d120a3-f05c-10ad-1ee9-c36682c528d5', 'state': 'running', 'source': {'name': 'PREMIERE OESTE', 'id': '85aaf033-dcfa-4406-b052-3f47a50f388a', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.88.17.35', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.35', 'encryption': 'none', 'usedBandwidth': '10.216', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC-02', 'id': '3bb3b385-3891-49e8-adb7-972c895f9aa2', 'protocol': 'srt', 'port': 10053, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 1000, 'srtConnectionLimit': 0, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 1, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '10.216', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '54_ABC_CBC_U-1577 -UNCO_P ', 'elapsedTime': '5695:56:13', 'id': 'e4a390c3-0ccb-4fd8-a48b-8bfcd913bbbc', 'label': '4af790e1-88df-b5d0-2f3a-f28312f08460', 'state': 'running', 'source': {'name': 'U-CRIME-LA-T2_P', 'id': 'b9c412bd-95cb-4a47-a338-1bb6ac1c4828', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.92.17.35', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.35', 'encryption': 'none', 'usedBandwidth': '10.216', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC-02', 'id': 'babde300-e7bc-4104-9076-b827b8813eb1', 'protocol': 'srt', 'port': 10054, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES128', 'srtLatency': 1000, 'srtConnectionLimit': 0, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 1, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '10.217', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '55_CANELA_ABC_Pri', 'elapsedTime': '1174:33:45', 'id': '931141d0-0139-4c9d-bf13-69a9b1cdeffc', 'label': 'cebe166a-642f-db3d-41ee-eb3c16e911b2', 'state': 'running', 'source': {'name': 'CANELA', 'id': '73ed6c6d-a8ed-4db1-af82-a5242b058b69', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '190.12.54.171', 'protocol': 'srt', 'port': 1021, 'encryption': 'none', 'usedBandwidth': '9.847', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CANELA', 'id': '0f9b690b-248a-45a3-85f3-0864efb49ee8', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.55', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '9.920', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 15000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '60_Test_CS:GO-ABC', 'elapsedTime': '00:00:41', 'id': '87587ab5-3bdc-4469-a20a-afa8a1f2ca66', 'label': 'a03fad04-666e-fe3c-f153-8375544ec1f7', 'state': 'idle', 'source': {'name': 'Test CS:Go', 'id': '76f32162-d3ee-45d0-91b0-e15f6b4ab7f6', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '190.104.233.219', 'protocol': 'srt', 'port': 10000, 'encryption': 'none', 'usedBandwidth': '0.0', 'state': 'connecting', 'srtLatency': 125, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped'}, 'destinations': [{'name': 'RCV 21', 'id': '9a4c4302-e968-48dd-9034-dee2b9ef1b16', 'protocol': 'udp', 'port': 10000, 'started': False, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.60', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'disconnected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '0.0', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'idle'}, {'name': '61_CBC02_ABC04_TEST', 'elapsedTime': '289:09:00', 'id': 'a1143c9b-ed29-4f4f-9976-cdf63065867e', 'label': '264efaab-2b59-ab8f-5b82-c0b34d7d2d2e', 'state': 'running', 'source': {'name': 'CBC02', 'id': '9df8eefa-d0a9-4866-a5a9-e84a6f71d4a9', 'networkInterface': '', 'mode': 'listener', 'address': '0.0.0.0', 'protocol': 'srt', 'port': 10044, 'encryption': 'srt', 'usedBandwidth': '8.178', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'srtPassPhrase': 'directv2420', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'RCV 24B', 'id': '272f3946-b361-4966-b86b-9cada93c5da6', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.61', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '8.173', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '62_COBC02-ABC04_EVC01-P3', 'elapsedTime': '169:43:38', 'id': '4c5463b1-7656-474b-addd-479859b66716', 'label': '768a2a62-94aa-950e-8fe9-1de9c3f4552a', 'state': 'running', 'source': {'name': 'COBC02', 'id': 'f7d4582a-ebb8-42b6-bd26-ac5ef7df4e3e', 'networkInterface': 'ens33', 'mode': 'listener', 'address': '0.0.0.0', 'protocol': 'srt', 'port': 10050, 'encryption': 'none', 'usedBandwidth': '2.089', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'lan', 'id': '7ada3062-1f84-4c4a-b829-452982338616', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.62', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '2.073', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '63_PRG_ABC04_NEWS', 'elapsedTime': '121:35:37', 'id': '09bf40a2-786a-4cee-9dbc-d8c25128f34a', 'label': 'cb2c22b1-55eb-d7b7-423f-c8083b4a7084', 'state': 'running', 'source': {'name': 'PRG', 'id': '88228dd3-9522-4335-aa3e-c17687c14f2d', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '190.104.242.106', 'protocol': 'srt', 'port': 10063, 'encryption': 'srt', 'usedBandwidth': '9.012', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': 'directv2420', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'RCV', 'id': 'd017d544-af60-41c5-8e21-e6db2fc3e2bb', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.63', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '8.916', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}]



"""


respuesta = [{'name': '01_ABC3_COBC1_TEST'
, 'elapsedTime': '4042:19:53'
, 'id': 'aba454e5-a2d5-4f2f-a82e-2fda732e796b'
, 'label': '284cc369-11bf-d856-f13a-58b32fc5e352'
, 'state': 'idle'
, 'source': {'name': 'h1', 'id': '22a819ab-ee3b-4a6e-8392-5f3ab2ca9612', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.77.17.170', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.170', 'encryption': 'none', 'usedBandwidth': '0.0', 'state': 'disconnected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped'}
, 'destinations': [{'name': 'COBC1', 'id': 'ab4b971b-f940-48a3-9cf6-43c02bdd7404', 'protocol': 'srt', 'port': 14056, 'started': False, 'mode': 'caller', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '191.102.238.101', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'disconnected', 'srtEncryption': 'None', 'srtLatency': 1002, 'srtOverhead': '25', 'srtPassPhrase': '', 'retainHeader': False, 'srtGroupMode': 'none', 'useFec': False, 'usedBandwidth': '0.0', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped'}]
, 'summaryStatusCode': 'unknown'
, 'summaryStatusDetails': 'idle'}
, {'name': '02_Test Haivision Canada'
, 'elapsedTime': '4919:25:47'
, 'id': 'b253ec0c-7f61-408f-8dc9-3b509294ffbd'
, 'label': '6568b65c-fba1-96b6-dc2d-6d8364faba3d'
, 'state': 'running', 'source': {'name': 'Makito X1 Canada', 'id': '7e066bac-5b97-45cf-a17e-1fc0bbd12546', 'networkInterface': 'ens33', 'mode': 'listener', 'address': '0.0.0.0', 'protocol': 'srt', 'port': 10003, 'encryption': 'none', 'usedBandwidth': '0.0', 'state': 'connecting', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'warn', 'summaryStatusDetails': 'connecting'}, 'destinations': [{'name': '02_Test Haivision Canada', 'id': '62ffa83d-16de-44fc-9aba-e1bc810a6224', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.2', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'disconnected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '0.000', 'summaryStatusCode': 'warn', 'summaryStatusDetails': 'disconnected from stream 238.77.24.2', 'shaping': True, 'maxBitrate': 10000}], 'summaryStatusCode': 'warn', 'summaryStatusDetails': 'Source Makito X1 Canada connecting'}, {'name': '04_ABC_INTER-TV_DTV-SPORTS-2_P', 'elapsedTime': '3839:39:21', 'id': '9011d5de-e145-4bee-a71a-c67142ca7832', 'label': 'e6a50430-a076-ab59-215d-5e1aded77bf7', 'state': 'running', 'source': {'name': 'DTV-SPORTS-2', 'id': '197a02d6-6711-4065-8e9f-738352aa542c', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '238.77.1.107', 'protocol': 'udp', 'port': 10000, 'sourceAddress': '10.77.22.197', 'encryption': 'none', 'usedBandwidth': '15.818', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'INTER-TV', 'id': '82444aef-9d06-4db6-a8cc-2ef7836023df', 'protocol': 'srt', 'port': 10037, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 2000, 'srtConnectionLimit': 5, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 2, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '15.818', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '05_ABC_INTER-TV_DTV-SPORTS-PLUS_P', 'elapsedTime': '3817:24:45', 'id': '1cf31869-5b98-45d7-81d5-58f0cca78bf1', 'label': 'a6cfa143-4c4c-efd3-54d9-08827eec2b7c', 'state': 'running', 'source': {'name': 'DTVSPORTS-PLUS', 'id': '79a99e00-7ca8-4dd5-9811-7e828769dc8c', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '238.77.1.108', 'protocol': 'udp', 'port': 10000, 'sourceAddress': '10.77.22.197', 'encryption': 'none', 'usedBandwidth': '15.819', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'INTER-TV', 'id': 'f46528b8-6df7-4a53-a753-579f975e5cdc', 'protocol': 'srt', 'port': 10038, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 2000, 'srtConnectionLimit': 5, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 2, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '15.818', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '06_ABC_INTER-TV_DTV-SPORTS-PAN_P', 'elapsedTime': '3839:37:20', 'id': 'cfb1912f-39a3-4fa0-bac6-312fa3a58150', 'label': '1eed7072-0ddc-b6f0-5822-5521ebabf166', 'state': 'running', 'source': {'name': 'DTV-SPORTS-PAN', 'id': 'e3c59b7e-fe9b-4ad5-98de-dec888eed440', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '238.77.1.104', 'protocol': 'udp', 'port': 10000, 'sourceAddress': '10.77.22.197', 'encryption': 'none', 'usedBandwidth': '15.816', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'INTER-TV', 'id': '120bb2c4-dd74-4f12-b0b0-70c3a463888a', 'protocol': 'srt', 'port': 10039, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 2000, 'srtConnectionLimit': 5, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 2, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '15.828', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '11_LaRed-Chile-B_ABC', 'elapsedTime': '00:00:33', 'id': '781612a7-06fe-449d-a7b3-85d47fb97e1d', 'label': 'bea0b4de-e60e-96e0-0cc6-7b8bea3e02ca', 'state': 'idle', 'source': {'name': 'LaRed-Chile-B', 'id': '52990479-4e52-4870-b59e-225ad70806cf', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '200.68.48.203', 'protocol': 'srt', 'port': 9005, 'encryption': 'srt', 'usedBandwidth': '0.0', 'state': 'disconnected', 'srtLatency': 1000, 'srtRcvBuf': 20240000, 'useFec': False, 'srtPassPhrase': 'directv2420', 'srtGroupMode': 'none', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped'}, 'destinations': [{'name': 'RCV-ABC-1209-B', 'id': 'a5d100b0-7258-468d-a75a-47c932d1a655', 'protocol': 'udp', 'port': 10000, 'started': False, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.11', 'ttl': 64, 'mtu': 1496, 'tos': 128, 'state': 'disconnected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '0.0', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'idle'}, {'name': '31_Campo_Rural_TV_ABC_B', 'elapsedTime': '1320:24:45', 'id': 'ca0240c3-8bb5-44ce-ae6e-d35aa2d63c81', 'label': '92f0b837-0ea2-413a-fe22-8e22372f451a', 'state': 'running', 'source': {'name': 'Campo Rural TV ABC B', 'id': '0c30c14d-0da8-49a7-8938-78a382ab5dcd', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '201.217.149.66', 'protocol': 'srt', 'port': 10028, 'encryption': 'none', 'usedBandwidth': '10.652', 'state': 'connected', 'srtLatency': 6000, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'RCV1274B', 'id': '7a80aaff-56ad-48e2-9a8a-ec76fe227967', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.31', 'ttl': 64, 'mtu': 1496, 'tos': 128, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '10.643', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': True, 'maxBitrate': 15000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '40_TELETUYA_GOLDDATA_ABC', 'elapsedTime': '1344:07:56', 'id': 'e3530418-f8de-4033-be38-ed9e47ebff68', 'label': '93fc3d93-30e4-9ad1-ae7f-f7245664ba10', 'state': 'running', 'source': {'name': 'TLT-GOLDDATA', 'id': '7f14c813-c9eb-4b2a-9c79-264431064ac0', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '10.202.30.1', 'protocol': 'srt', 'port': 10040, 'encryption': 'none', 'usedBandwidth': '6.645', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'VOS', 'id': '409e8480-337b-4f09-afc4-40f6a4999b77', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.40', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '6.619', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '41_ABC04_CBC02_MTV00_B_TEST', 'elapsedTime': '2644:49:34', 'id': 'f81e690b-7a90-49ba-a4d9-b8312f71477f', 'label': '49bc62a3-f6e2-a9e9-5df5-ebf888c94120', 'state': 'running', 'source': {'name': 'RCV1356_MTV00_B', 'id': '32b3f922-ae9c-4990-bb5c-28a1bd9fe342', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.77.17.164', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.164', 'encryption': 'none', 'usedBandwidth': '20.429', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC02_MTV00', 'id': 'fd06d0b8-1bcb-4adf-9895-1f860078243a', 'protocol': 'srt', 'port': 10020, 'started': True, 'mode': 'caller', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '99.193.236.205', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'None', 'srtLatency': 1000, 'srtOverhead': '25', 'srtPassPhrase': '', 'retainHeader': False, 'srtGroupMode': 'none', 'useFec': False, 'usedBandwidth': '20.429', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '42_ABC04_CBC02_TeenNick_B_TEST', 'elapsedTime': '2644:41:31', 'id': '550ebe6f-1a8c-4af8-98c8-e05e88ce430c', 'label': '18948d98-c10f-64eb-dced-63a099031fba', 'state': 'running', 'source': {'name': 'rcv1354_TeenNick_B', 'id': '2da7d492-9656-4bb8-b9bf-f229222c2ff1', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.77.17.162', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.162', 'encryption': 'none', 'usedBandwidth': '15.324', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC02-Teen Nick', 'id': 'c5bdb076-1fe8-4734-832e-aa32d94938f9', 'protocol': 'srt', 'port': 10021, 'started': True, 'mode': 'caller', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '99.193.236.205', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'None', 'srtLatency': 1000, 'srtOverhead': '25', 'srtPassPhrase': '', 'retainHeader': False, 'srtGroupMode': 'none', 'useFec': False, 'usedBandwidth': '15.324', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '51_ABC_CBC_U-1574-UNCE_P ', 'elapsedTime': '5711:57:37', 'id': 'd34cd9d2-e9c9-4bbe-a20a-d5fe6be00137', 'label': 'ac6db064-f459-a4fd-6e1b-9d0dd4780a22', 'state': 'running', 'source': {'name': 'CRIME ESTE', 'id': '09a6c3f6-fdf8-4062-8f83-184ec78ab525', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.82.17.35', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.35', 'encryption': 'none', 'usedBandwidth': '10.216', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC-01', 'id': '516375ed-0571-4b4e-ac71-d72646b00e91', 'protocol': 'srt', 'port': 10051, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 1000, 'srtConnectionLimit': 0, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 1, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '10.216', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '52_ABC_CBC_U-1575-UNRE_B', 'elapsedTime': '5711:56:47', 'id': '7350f3b1-364b-4390-a54a-1217bf17eab3', 'label': '6da4723a-afb4-9355-3204-09267b29fbf5', 'state': 'running', 'source': {'name': 'REALITY', 'id': '092764e0-2e59-4849-a1a3-17cbd3de453c', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.80.17.35', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.35', 'encryption': 'none', 'usedBandwidth': '10.216', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC-02', 'id': '606dfba9-79e8-439f-9315-8cf9688de291', 'protocol': 'srt', 'port': 10052, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 1000, 'srtConnectionLimit': 0, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 1, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '10.216', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '53_ABC_CBC_U-1576-UPRO_P ', 'elapsedTime': '818:35:14', 'id': '28e9abe8-80cb-469c-8baf-b76717ec26ee', 'label': 'f4d120a3-f05c-10ad-1ee9-c36682c528d5', 'state': 'running', 'source': {'name': 'PREMIERE OESTE', 'id': '85aaf033-dcfa-4406-b052-3f47a50f388a', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.88.17.35', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.35', 'encryption': 'none', 'usedBandwidth': '10.216', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC-02', 'id': '3bb3b385-3891-49e8-adb7-972c895f9aa2', 'protocol': 'srt', 'port': 10053, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES256', 'srtLatency': 1000, 'srtConnectionLimit': 0, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 1, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '10.216', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '54_ABC_CBC_U-1577 -UNCO_P ', 'elapsedTime': '5695:56:13', 'id': 'e4a390c3-0ccb-4fd8-a48b-8bfcd913bbbc', 'label': '4af790e1-88df-b5d0-2f3a-f28312f08460', 'state': 'running', 'source': {'name': 'U-CRIME-LA-T2_P', 'id': 'b9c412bd-95cb-4a47-a338-1bb6ac1c4828', 'networkInterface': 'ens34', 'mode': 'multicast', 'address': '239.92.17.35', 'protocol': 'udp', 'port': 8999, 'sourceAddress': '10.77.23.35', 'encryption': 'none', 'usedBandwidth': '10.216', 'state': 'connected', 'srtRcvBuf': 10240000, 'srtPassPhrase': None, 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CBC-02', 'id': 'babde300-e7bc-4104-9076-b827b8813eb1', 'protocol': 'srt', 'port': 10054, 'started': True, 'mode': 'listener', 'networkAddress': None, 'networkInterface': 'ens33', 'address': '0.0.0.0', 'ttl': 64, 'mtu': 1496, 'tos': 104, 'state': 'connected', 'srtEncryption': 'AES128', 'srtLatency': 1000, 'srtConnectionLimit': 0, 'srtOverhead': '25', 'srtPassPhrase': 'directv2420', 'clientConnections': 1, 'retainHeader': False, 'srtGroupMode': 'none', 'usedBandwidth': '10.217', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '55_CANELA_ABC_Pri', 'elapsedTime': '1174:33:45', 'id': '931141d0-0139-4c9d-bf13-69a9b1cdeffc', 'label': 'cebe166a-642f-db3d-41ee-eb3c16e911b2', 'state': 'running', 'source': {'name': 'CANELA', 'id': '73ed6c6d-a8ed-4db1-af82-a5242b058b69', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '190.12.54.171', 'protocol': 'srt', 'port': 1021, 'encryption': 'none', 'usedBandwidth': '9.847', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'CANELA', 'id': '0f9b690b-248a-45a3-85f3-0864efb49ee8', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.55', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '9.920', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 15000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '60_Test_CS:GO-ABC', 'elapsedTime': '00:00:41', 'id': '87587ab5-3bdc-4469-a20a-afa8a1f2ca66', 'label': 'a03fad04-666e-fe3c-f153-8375544ec1f7', 'state': 'idle', 'source': {'name': 'Test CS:Go', 'id': '76f32162-d3ee-45d0-91b0-e15f6b4ab7f6', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '190.104.233.219', 'protocol': 'srt', 'port': 10000, 'encryption': 'none', 'usedBandwidth': '0.0', 'state': 'connecting', 'srtLatency': 125, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped'}, 'destinations': [{'name': 'RCV 21', 'id': '9a4c4302-e968-48dd-9034-dee2b9ef1b16', 'protocol': 'udp', 'port': 10000, 'started': False, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.60', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'disconnected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '0.0', 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'stopped', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'unknown', 'summaryStatusDetails': 'idle'}, {'name': '61_CBC02_ABC04_TEST', 'elapsedTime': '289:09:00', 'id': 'a1143c9b-ed29-4f4f-9976-cdf63065867e', 'label': '264efaab-2b59-ab8f-5b82-c0b34d7d2d2e', 'state': 'running', 'source': {'name': 'CBC02', 'id': '9df8eefa-d0a9-4866-a5a9-e84a6f71d4a9', 'networkInterface': '', 'mode': 'listener', 'address': '0.0.0.0', 'protocol': 'srt', 'port': 10044, 'encryption': 'srt', 'usedBandwidth': '8.178', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'srtPassPhrase': 'directv2420', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'RCV 24B', 'id': '272f3946-b361-4966-b86b-9cada93c5da6', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.61', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '8.173', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '62_COBC02-ABC04_EVC01-P3', 'elapsedTime': '169:43:38', 'id': '4c5463b1-7656-474b-addd-479859b66716', 'label': '768a2a62-94aa-950e-8fe9-1de9c3f4552a', 'state': 'running', 'source': {'name': 'COBC02', 'id': 'f7d4582a-ebb8-42b6-bd26-ac5ef7df4e3e', 'networkInterface': 'ens33', 'mode': 'listener', 'address': '0.0.0.0', 'protocol': 'srt', 'port': 10050, 'encryption': 'none', 'usedBandwidth': '2.089', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'srtPassPhrase': '', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'lan', 'id': '7ada3062-1f84-4c4a-b829-452982338616', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.62', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '2.073', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}, {'name': '63_PRG_ABC04_NEWS', 'elapsedTime': '121:35:37', 'id': '09bf40a2-786a-4cee-9dbc-d8c25128f34a', 'label': 'cb2c22b1-55eb-d7b7-423f-c8083b4a7084', 'state': 'running', 'source': {'name': 'PRG', 'id': '88228dd3-9522-4335-aa3e-c17687c14f2d', 'networkInterface': 'ens33', 'mode': 'caller', 'address': '190.104.242.106', 'protocol': 'srt', 'port': 10063, 'encryption': 'srt', 'usedBandwidth': '9.012', 'state': 'connected', 'srtLatency': 1000, 'srtRcvBuf': 10240000, 'useFec': False, 'srtPassPhrase': 'directv2420', 'srtGroupMode': 'none', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected'}, 'destinations': [{'name': 'RCV', 'id': 'd017d544-af60-41c5-8e21-e6db2fc3e2bb', 'protocol': 'udp', 'port': 10000, 'started': True, 'mode': 'multicast', 'networkAddress': None, 'networkInterface': 'ens34', 'address': '238.77.24.63', 'ttl': 64, 'mtu': 1496, 'tos': 136, 'state': 'connected', 'encryption': 'none', 'fec': 'none', 'usedBandwidth': '8.916', 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'connected', 'shaping': False, 'maxBitrate': 10000}], 'summaryStatusCode': 'ok', 'summaryStatusDetails': 'running'}
             ]






POST_ROUTE_REQUEST = [
    "name"
    , "id"
    , "source"
    , "destinations"]
GET_ROUTE_RESPONSE = [
    "name"
    , "id"
    , "source"
    , "destinations"
    , "elapsedTime"
    , "state"
    ,"pendingUpdates"
    ,"summaryStatusCode"
    ,"summaryStatusDetails"
    ,"hasPendingDelete"]
POST_SOURCE_UDP_REQUEST = [
    "name"
    ,"id"
    ,"address"
    ,"protocol"
    ,"port"
    ,"networkInterface"
    ,"retainHeader"
    ,"sourceAddress"
    ,"fec"]
POST_SOURCE_SRT_REQUEST = [
    "name"
    ,"id"
    ,"address"
    ,"protocol"
    ,"port"
    ,"networkInterface"
    ,"srtPassPhrase"
    ,"srtLatency"
    ,"srtMode"
    ,"srtRcvBuf"
    ,"srtStreamID"
    ,"useFec"
    ,"srtFecCols"
    ,"srtFecRows"
    ,"srtFecLayout"
    ,"srtFecArq"
    ,"srtGroupMode"
    ,"srtNetworkBondingParams"]
GET_SOURCE_UDP_RESPONSE = [
    "name"
    ,"id"
    ,"address"
    ,"protocol"
    ,"port"
    ,"networkInterface"
    ,"retainHeader"
    ,"sourceAddress"
    ,"fec"
    ,"state"
    ,"summaryStatusCode"
    ,"summaryStatusDetails"]
GET_SOURCE_SRT_RESPONSE = [
    "name"
    ,"id"
    ,"address"
    ,"protocol"
    ,"port"
    ,"networkInterface"
    ,"srtPassPhrase"
    ,"srtLatency"
    ,"srtRcvBuf"
    ,"srtStreamID"
    ,"useFec"
    ,"srtFecCols"
    ,"srtFecRows"
    ,"srtFecLayout"
    ,"srtFecArq"
    ,"mode"
    ,"state"
    ,"summaryStatusCode"
    ,"summaryStatusDetails"
    ,"srtGroupMode"
    ,"srtNetworkBondingParams"]
POST_DEST_UDP_REQUEST = [
    "name"
    ,"id"
    ,"address"
    ,"protocol"
    ,"port"
    ,"networkInterface"
    ,"retainHeader"
    ,"action"
    ,"mtu"
    ,"ttl"
    ,"tos"
    ,"fec"
    ,"prompegFecLevel"
    ,"prompegFecIsBlockAligned"
    ,"prompegFecColumns"
    ,"prompegFecRows"
    ,"shaping"
    ,"maxBitrate"]
POST_DEST_SRT_REQUEST = [
    "name"
    ,"id"
    ,"address"
    ,"protocol"
    ,"port"
    ,"networkInterface"
    ,"retainHeader"
    ,"action"
    ,"mtu"
    ,"ttl"
    ,"tos"
    ,"srtEncryption"
    ,"srtPassPhrase"
    ,"srtLatency"
    ,"srtMode"
    ,"srtOverhead"
    ,"srtStreamID"
    ,"useFec"
    ,"srtFecCols"
    ,"srtFecRows"
    ,"srtFecLayout"
    ,"srtFecArq"
    ,"srtConnectionLimit"
    ,"srtGroupMode"
    ,"srtNetworkBondingParams"]
GET_DEST_UDP_RESPONSE = [
    "name"
    ,"id"
    ,"address"
    ,"protocol"
    ,"port"
    ,"networkInterface"
    ,"retainHeader"
    ,"mtu"
    ,"ttl"
    ,"tos"
    ,"fec"
    ,"prompegFecLevel"
    ,"prompegFecIsBlockAligned"
    ,"prompegFecColumns"
    ,"prompegFecRows"
    ,"shaping"
    ,"maxBitrate"
    ,"state"
    ,"summaryStatusCode"
    ,"summaryStatusDetails"
    ,"started"]
GET_DEST_SRT_RESPONSE = [
    "name"
    ,"id"
    ,"address"
    ,"protocol"
    ,"port"
    ,"networkInterface"
    ,"retainHeader"
    ,"mtu"
    ,"ttl"
    ,"tos"
    ,"srtEncryption"
    ,"srtPassPhrase"
    ,"useFEC"
    ,"srtFecCols"
    ,"srtFecRows"
    ,"srtFecLayout"
    ,"srtFecArq"
    ,"srtConnectionLimit"
    ,"srtLatency"
    ,"mode"
    ,"srtOverhead"
    ,"state"
    ,"summaryStatusCode"
    ,"summaryStatusDetails"
    ,"started"
    ,"srtStreamID"
    ,"srtGroupMode"
    ,"srtNetworkBondingParams"]









#print("fffffff=",GET_ROUTE_RESPONSE[1])
#print(GET_SOURCE_UDP_RESPONSE)
#print(p.POST_DEST_SRT_REQUEST)
#print(GET_SOURCE_SRT_RESPONSE)
#print(GET_DEST_UDP_RESPONSE)
#print(GET_DEST_SRT_RESPONSE)




lista_source_total = ['name', 'id', 'address', 'protocol', 'port', 'networkInterface', 'retainHeader', 'sourceAddress', 'fec', 'state', 'summaryStatusCode', 'summaryStatusDetails', 'srtPassPhrase', 'srtLatency', 'srtRcvBuf', 'srtStreamID', 'useFec', 'srtFecCols', 'srtFecRows', 'srtFecLayout', 'srtFecArq', 'mode', 'state', 'summaryStatusCode', 'summaryStatusDetails', 'srtGroupMode', 'srtNetworkBondingParams']
lista_dest_total = ['name', 'id', 'address', 'protocol', 'port', 'networkInterface', 'retainHeader', 'mtu', 'ttl', 'tos', 'fec', 'prompegFecLevel', 'prompegFecIsBlockAligned', 'prompegFecColumns', 'prompegFecRows', 'shaping', 'maxBitrate', 'state', 'summaryStatusCode', 'summaryStatusDetails', 'started', 'srtEncryption', 'srtPassPhrase', 'useFEC', 'srtFecCols', 'srtFecRows', 'srtFecLayout', 'srtFecArq', 'srtConnectionLimit', 'srtLatency', 'mode', 'srtOverhead', 'state', 'summaryStatusCode', 'summaryStatusDetails', 'started', 'srtStreamID', 'srtGroupMode', 'srtNetworkBondingParams']

#print(lista_dest_total)

lista2 = {lista_source_total[0]: respuesta[0]["source"]["name"]}
print(lista2)






















