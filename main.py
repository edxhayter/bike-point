from modules.log_functions import log_init
from modules.extract_functions import extract_json
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
logger = log_init('logs', timestamp, 1)
logger.info('Logger successfully initialised')
logger.debug('Debug mode initialised')

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'
max_retry = 5
delay = 10

extract_json(url, data_dir, timestamp, max_retry, delay)