from modules.log_functions import log_init
from modules.extract_functions import extract_json
from modules.load_functions import load_to_s3
from datetime import datetime
from dotenv import load_dotenv
import os

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
logger = log_init('logs', timestamp, 1)
logger.info('Logger successfully initialised')
logger.debug('Debug mode initialised')

# Extract Variables
url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'
max_retry = 5
delay = 10

# Load variables
load_dotenv()
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

extract_json(url, data_dir, timestamp, max_retry, delay)
load_to_s3(data_dir, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME)   
