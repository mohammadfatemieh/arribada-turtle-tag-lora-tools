import sys
import logging
from arribada_tools import gps_config

logging.basicConfig(format='%(asctime)s\t%(module)s\t%(levelname)s\t%(message)s', level=logging.DEBUG)

backend = gps_config.GPSSerialBackend(sys.argv[1], baudrate=int(sys.argv[2]))
backend.read(1024)

ascii_data = open(sys.argv[3], 'rb').read()
cfg = gps_config.GPSConfig(backend)
cfg.ascii_config_session(ascii_data)
