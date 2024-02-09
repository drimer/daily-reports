import os
from unittest.mock import Mock
from src.config import Config


def test_config():
    class TestConfig(Config):
        def __init__(self) -> None:
            self.TEST_PARAM = self.get_from_env('TEST_PARAM')

    env_value = 'test_value'
    os.environ.get = Mock(return_value=env_value)

    config = TestConfig()

    os.environ.get.assert_called_once_with('TEST_PARAM')
    assert config.TEST_PARAM == env_value
