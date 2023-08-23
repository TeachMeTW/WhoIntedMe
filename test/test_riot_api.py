import pytest
from unittest.mock import patch, Mock
from back.riot_api import (
    get_all_matches,
    get_single_match,
    get_user,
    recent_match_ids,
    match_data,
)


@pytest.mark.parametrize(
    "mock_return_value, expected_result, exception",
    [
        ({"id": "12345"}, {"id": "12345"}, None),
        (500, None, Exception),
        ({}, None, KeyError),
    ],
)
@patch("back.riot_api.requests.get")
def test_get_user(mock_get, mock_return_value, expected_result, exception):
    mock_response = Mock()

    if isinstance(mock_return_value, int):
        mock_response.status_code = mock_return_value
    else:
        mock_response.json.return_value = mock_return_value
        mock_response.status_code = (
            200  # Ensure the status code is 200 for non-exception cases
        )

    mock_get.return_value = mock_response

    if exception:
        with pytest.raises(exception):
            get_user("TestUser")
    else:
        result = get_user("TestUser")
        assert result == expected_result


@pytest.mark.parametrize(
    "mock_return_value, expected_length, exception",
    [
        (["match1", "match2"], 2, None),
        ([], 0, None),
        ({"unexpected_key": "unexpected_value"}, None, Exception),
    ],
)
@patch("back.riot_api.requests.get")
def test_recent_match_ids(mock_get, mock_return_value, expected_length, exception):
    mock_response = Mock()
    mock_response.json.return_value = mock_return_value
    mock_response.status_code = (
        200 if isinstance(mock_return_value, (list, dict)) else mock_return_value
    )
    mock_get.return_value = mock_response

    if exception:
        with pytest.raises(exception):
            recent_match_ids("puuidTest")
    else:
        result = recent_match_ids("puuidTest")
        assert len(result) == expected_length


@pytest.mark.parametrize(
    "mock_return_value, expected_result, exception",
    [
        (
            {
                "metadata": {"data_key1": "data_value1"},
                "info": {"info_key1": "info_value1"},
            },
            {
                "metadata": {"data_key1": "data_value1"},
                "info": {"info_key1": "info_value1"},
            },
            None,
        ),
        ({"unexpected_key": "unexpected_value"}, None, KeyError),
        (500, None, Exception),
    ],
)
@patch("back.riot_api.requests.get")
def test_match_data(mock_get, mock_return_value, expected_result, exception):
    mock_response = Mock()
    mock_response.json.return_value = mock_return_value
    mock_response.status_code = (
        200 if isinstance(mock_return_value, dict) else mock_return_value
    )
    mock_get.return_value = mock_response

    if exception:
        with pytest.raises(exception):
            match_data("matchIdTest")
    else:
        result = match_data("matchIdTest")
        assert result == expected_result


@patch("back.riot_api.match_data")
@patch("back.riot_api.recent_match_ids")
@patch("back.riot_api.get_user")
def test_get_single_match(mock_get_user, mock_recent_match_ids, mock_match_data):
    mock_get_user.return_value = {"puuid": "test123"}
    mock_recent_match_ids.return_value = ["match1"]

    mock_data = {
        "metadata": {"participants": ["player1"]},
        "info": {"gameId": "123456"},
    }
    mock_match_data.return_value = mock_data

    result = get_single_match("TestUser")
    assert result["gameId"] == "123456"


@patch("back.riot_api.match_data")
@patch("back.riot_api.recent_match_ids")
@patch("back.riot_api.get_user")
def test_get_all_matches(mock_get_user, mock_recent_match_ids, mock_match_data):
    mock_get_user.return_value = {"puuid": "test123"}
    mock_recent_match_ids.return_value = ["match1", "match2"]

    mock_data1 = {
        "metadata": {"participants": ["player1"]},
        "info": {"gameId": "123456"},
    }

    mock_data2 = {
        "metadata": {"participants": ["player2"]},
        "info": {"gameId": "654321"},
    }

    mock_match_data.side_effect = [mock_data1, mock_data2]

    results = get_all_matches("TestUser")
    assert len(results) == 2
    assert results[0]["gameId"] == "123456"
    assert results[1]["gameId"] == "654321"
