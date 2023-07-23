import data

test_uri = "sqlite:///test_flights.sqlite3"

test_flight_class = data.FlightData(test_uri)


def test_get_all_delayed_flights_by_airlines():
    flights = test_flight_class.get_all_delayed_flights_by_airlines()
    delta_airline_flight = next((flight for flight in flights if flight['AIRLINE'] == 'Delta Air Lines Inc.'), None)
    assert len(flights) == 13
    assert delta_airline_flight['DELAY_PERCENTAGE'] == 20.326802357381666
