import visuals
import data

test_uri = "sqlite:///test_flights.sqlite3"

test_flight_data = data.FlightData(test_uri)


def test_percentage_delayed_flights_by_airline():
    flights = test_flight_data.get_all_delayed_flights_by_airlines()
    visuals.percentage_delayed_flights_by_airline(flights)
