import pytest
from CS50p.project.project import fetch_astronaut_data, retry_on_timeout

@pytest.fixture
def sample_astronaut_data():
    return {
        "number": 3,
        "people": [
            {"name": "Astronaut 1"},
            {"name": "Astronaut 2"},
            {"name": "Astronaut 3"},
        ],
    }

def test_fetch_astronaut_data_success(requests_mock, sample_astronaut_data):
    requests_mock.get("http://api.open-notify.org/astros.json", json=sample_astronaut_data)
    data = fetch_astronaut_data("http://api.open-notify.org/astros.json")
    assert len(data) == 3
    assert data[0]["name"] == "Astronaut 1"

def test_fetch_astronaut_data_failure(requests_mock):
    requests_mock.get("http://api.open-notify.org/astros.json", exc=Exception("Test error"))
    data = fetch_astronaut_data("http://api.open-notify.org/astros.json")
    assert len(data) == 0

def test_retry_on_timeout(requests_mock):
    def fake_request_timeout():
        raise TimeoutError("Test timeout")

    wrapped_request = retry_on_timeout()(fake_request_timeout)
    with pytest.raises(TimeoutError):
        wrapped_request()
        assert requests_mock.request_history[0].method == "GET"

if __name__ == "__main__":
    pytest.main()
