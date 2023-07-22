from sqlalchemy import create_engine, text

QUERY_FLIGHT_BY_ID = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY " \
                     "FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.ID = :id"

QUERY_FLIGHTS_BY_DATE = "SELECT flights.*, airlines.airline, flights.DEPARTURE_DELAY as DELAY " \
                        "FROM flights JOIN airlines ON flights.airline = airlines.id " \
                        "WHERE flights.DAY = :day AND flights.MONTH = :month AND flights.YEAR = :year"

QUERY_DELAYED_FLIGHTS_BY_AIRLINE = "SELECT flights.*, airlines.airline, flights.DEPARTURE_DELAY as DELAY " \
                                   "FROM flights JOIN airlines " \
                                   "ON flights.airline = airlines.id WHERE airlines.airline = :airline_name"

QUERY_DELAYED_FLIGHTS_BY_AIRPORT = "SELECT flights.*, airlines.airline, flights.DEPARTURE_DELAY as DELAY " \
                                   "FROM flights JOIN airlines ON flights.airline = airlines.id " \
                                   "WHERE flights.ORIGIN_AIRPORT = :airport_code"


class FlightData:
    """
    The FlightData class is a Data Access Layer (DAL) object that provides an
    interface to the flight data in the SQLITE database. When the object is created,
    the class forms connection to the sqlite database file, which remains active
    until the object is destroyed.
    """

    def __init__(self, db_uri):
        """
        Initialize a new engine using the given database URI
        """
        self._engine = create_engine(db_uri)

    def _execute_query(self, query, params=None):
        """
        Execute an SQL query with the params provided in a dictionary,
        and returns a list of records (dictionary-like objects).
        If an exception was raised, print the error, and return an empty list.
        """

        if params is None:
            params = []
        with self._engine.connect() as connection:
            try:
                results = connection.execute(text(query), params)
                rows = results.fetchall()
                records = [row._asdict() for row in rows]
                return records
            except Exception as e:
                print(f'Error executing query, {e}')
                return []

    def get_flight_by_id(self, flight_id):
        """
        Searches for flight details using flight ID.
        If the flight was found, returns a list with a single record.
        """
        params = {'id': flight_id}
        return self._execute_query(QUERY_FLIGHT_BY_ID, params)

    def __del__(self):
        """
        Closes the connection to the database when the object is about to be destroyed
        """
        self._engine.dispose()

    def get_flights_by_date(self, day, month, year):
        """
            Searches for flight details using date
            If there are flights on the search date found, returns a list with the record(s).
        """
        params = {'day': day, 'month': month, 'year': year}
        return self._execute_query(QUERY_FLIGHTS_BY_DATE, params)

    def get_delayed_flights_by_airline(self, airline_input):
        """
            Searches for delayed flights of a certain airline, and returns any found as a list.
        """
        params = {'airline_name': airline_input}
        return self._execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRLINE, params)

    def get_delayed_flights_by_airport(self, airport):
        """
            Searches for delayed flights from a specific airport, and returns any found as a list.
        """
        params = {'airport_code': airport}
        return self._execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRPORT, params)
