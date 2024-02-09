import os


class ConfigError(Exception):
    pass


class Config:
    def get_from_env(self, param_name) -> str:
        value = os.environ.get(param_name)

        if value is None:  # TBD
            raise ConfigError('Could not get the value for env variable {}'.format(param_name))

        return value
