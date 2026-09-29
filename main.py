from modules.log_functions import log_init
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
logger = log_init('logs', timestamp, 1)
logger.info('Logger successfully initialised')
logger.debug('Debug mode initialised')