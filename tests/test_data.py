import data

test_uri = "sqlite:///test_flights.sqlite3"

test_flight_class = data.FlightData(test_uri)


def test_get_all_delayed_flights():
    result = test_flight_class.get_all_delayed_flights()
    assert len(result) != 0
    assert result[0]['ID'] == 8
    assert result[0]['ORIGIN_AIRPORT'] == 'LAX'
    print(result[0])
    for flight in result:
        assert flight['DEPARTURE_DELAY'] != ''
        assert int(flight['DEPARTURE_DELAY']) > 0
