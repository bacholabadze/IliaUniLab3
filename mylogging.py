import logging

# logging.basicConfig(level= logging.DEBUG)
logging.basicConfig(filename='./app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level= logging.DEBUG)

logging.debug('This will get logged')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')
logging.info('This is info message')
