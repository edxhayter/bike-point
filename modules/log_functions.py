import os
import logging

def log_init(log_dir:str, timestamp:str, debug_mode:bool):
    """
    Initialises the logging functionality

    Args:
        log_dir(str): What sub-directory to save the logs to.
        timestamp(str): Timestamp to use for the log file name.
        debugmode(bool): 1 when running in debug mode to also return debug messages
    """
    os.makedirs(log_dir,exist_ok=True)
    log_filename = f'{log_dir}/{timestamp}.log'

    logging.basicConfig(
        filename=log_filename,
        format = '%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO if debug_mode==0 else logging.DEBUG
    )

    return logging.getLogger()