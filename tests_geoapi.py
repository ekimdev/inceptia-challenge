from geoapi import GeoAPI


def test_is_hot_in_pehuajo(monkeypatch):
    def mock_request_weather_info(url):
        _ = url
        return {"main": {"temp": 29}}

    monkeypatch.setattr(GeoAPI, "request_weather_info", mock_request_weather_info)

    response = GeoAPI.is_hot_in_pehuajo()
    assert response


def test_is_not_hot_in_pehuajo(monkeypatch):
    def mock_request_weather_info(url):
        _ = url
        return {"main": {"temp": 26}}

    monkeypatch.setattr(GeoAPI, "request_weather_info", mock_request_weather_info)

    response = GeoAPI.is_hot_in_pehuajo()
    assert not response
