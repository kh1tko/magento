import logging
import os


class LogInfo:
    @staticmethod
    def logGen():
        current_dir = os.path.dirname(__file__)
        log_dir = os.path.join(current_dir, '..', 'Logs')

        log_file = os.path.join(log_dir, 'log1.log')
        logging.basicConfig(filename=log_file, level=logging.DEBUG,
                            format='%(asctime)s: %(levelname)s:%(message)s', datefmt='%m/%d/%Y�%I:%M:%S�%p')
        return logging.getLogger()
