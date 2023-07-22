import unittest
from data import FlightData

SQLITE_URI = 'sqlite:///test_flights.sqlite3'


class TestFlightData(unittest.TestCase):
    def setUp(self):
        # Create an instance of the FlightData class for testing
        self.flight_data = FlightData(SQLITE_URI)

    def test_get_flight_by_id(self):
        # Test case for get_flight_by_id function
        # Assuming there's a flight with ID 1 in the database
        flight_id = 1
        result = self.flight_data.get_flight_by_id(flight_id)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIn('FLIGHT_ID', result[0])
        self.assertIn('ORIGIN_AIRPORT', result[0])
        self.assertIn('DESTINATION_AIRPORT', result[0])
        self.assertIn('AIRLINE', result[0])
        self.assertIn('DELAY', result[0])

        # Assuming there's no flight with ID 1000000 in the database
        non_existent_id = 1000000
        result = self.flight_data.get_flight_by_id(non_existent_id)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_execute_query(self):
        # Test case for _execute_query function
        # Assuming there's a table named 'flights' in the database
        query = "SELECT * FROM flights WHERE id = :id"
        params = {'id': 1}
        result = self.flight_data._execute_query(query, params)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

        # Test with a non-existing record
        params = {'id': 1000000}
        result = self.flight_data._execute_query(query, params)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def tearDown(self):
        # Clean up any resources after each test case
        self.flight_data._engine.dispose()


if __name__ == "__main__":
        unittest.main()
