from unittest.mock import Mock

from  unittest_examples.mock_example import get_user

def test_get_user_mock():
    api = Mock()
    api.get.return_value = {"id": 1, "name": "John"}

    result = get_user(api, 1)
    assert result["name"] == "John"
