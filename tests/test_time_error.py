import time
from unittest.mock import Mock
from lib.time_error import TimeError

def test_returns_error():
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = time.time()

    time_error = TimeError(requester_mock)
    result = time_error.error()
    # assert result == 10.0