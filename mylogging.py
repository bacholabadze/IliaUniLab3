import logging
import sys
import inspect

try:
    print("Shesadzlebelia kodis gashveba =>>>> python mylogging.py log_name.log a")
    print(f"Gadacemuli Argumentebia: {sys.argv[1:]}")
    log_file_name = str(sys.argv[1])
    log_file_mode = str(sys.argv[2])
    # logging.basicConfig(level= logging.DEBUG)
    logging.basicConfig(filename=log_file_name, filemode=log_file_mode, format='%(name)s - %(levelname)s - %(message)s', level= logging.DEBUG)
except:
    logging.basicConfig(filename="app.log", filemode="w", format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)

logging.debug('This will get logged')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')
logging.info(f'This is info message. Line NO: {inspect.currentframe().f_lineno}')
