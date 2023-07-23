import matplotlib.pyplot as plt


def percentage_delayed_flights_by_airline(airline_flights):
    airlines = [flight['AIRLINE'] for flight in airline_flights]
    delay_percentages = [flight['DELAY_PERCENTAGE'] for flight in airline_flights]

    plt.bar(airlines, delay_percentages)
    plt.xlabel('Airlines')
    plt.ylabel('Delay Percentage')
    plt.title('Delay Percentage by Airline')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.tight_layout()
    plt.show()


class FlightVisuals:
    """
    The FlightVisuals class takes data input from the FlightData class and uses python library to create
    graphs and visualisations of that data.
    """

    def __init__(self):
        pass
