
import logging
import logging.config


from variconfig.core.config import ConfigDict

class LoggingConfig(ConfigDict):
    def __init__(self, dictionary: dict):
        super().__init__(dictionary)
        self._update_logger()

    def __setattr__(self, key, value):
        object.__setattr__(key, value)
        self._update_logger()

    def _update_logger(self):
        try:
            logging_config=self.logging_config.to_dict()
            logging_config
            logging.config.dictConfig(self.logging_config.to_dict())
            logging.info(f"Logger configuration updated: {self.logging_config.to_dict()}")
        except Exception as e:
            logging.exception(f"Failed to update logger configuration: {e}")

    def _update_logger(self):
        try:
            logging.config.dictConfig(self.to_dict())
            logging.info(f"Logger configuration updated: {self.to_dict()}")
        except Exception as e:
            logging.error(f"Failed to update logger configuration: {e}")

    def update(self, dictionary):
        super().update(dictionary)
        self._update_logger()
