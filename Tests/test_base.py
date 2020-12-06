import pytest
from Utils.Logging.logging import logBase


@pytest.mark.usefixtures("init_driver")
class BaseTest(logBase):
    pass
