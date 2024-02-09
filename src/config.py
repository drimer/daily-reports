import os


class ConfigError(Exception):
    pass


class Config:
    def get_from_env(self, param_name) -> str:
        value = os.environ.get(param_name)

        if value is None:  # TBD
            raise ConfigError('Could not get the value for env variable {}'.format(param_name))

        return value


# def test_config():
#     class TestConfig(Config):
#         TEST_PARAM: str = Config.get_from_env('TEST_PARAM')
#
#     env_value = 'test_value'
#     os.environ.get = Mock(return_value=env_value)
#
#     config = TestConfig()
#
#     os.environ.get.assert_called_once_with('TEST_PARAM')
#     assert config.TEST_PARAM == env_value
