import logging
import pdb


class LogGen:

    @staticmethod
    def loggen():
        # pdb.set_trace()
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt='%m-%d-%Y %I:%M:%S %p',
                            force=True)
        # pdb.set_trace()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
