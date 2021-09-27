import logging

# asctime  - it will give you date and time of log
# levelname - it will give you log level printed in code. i.e. info, debug,error, critical, warning
# message - it will give you whatever developer wanted to print the message
# datefmt - it is used to change date and time format

logging.basicConfig(filename="test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/ %d/ %Y %I:%M:%S %p',
                    level=logging.DEBUG)

logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.debug("DEBUG")
logging.critical("CRITICAL")
