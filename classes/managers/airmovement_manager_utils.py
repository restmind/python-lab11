from classes.managers.sort_type import SortType
from classes.models.helicopter import Helicopter
from classes.models.passenger_airplane import PassengerAirplane
from classes.models.transport_airplane import TransportAirplane


class AirmovementManagerUtils:

    @staticmethod
    def find_aircraft_price_lower_than(entry_list, price_to_compare: float):
        """
        Find aircraft with lower price than 1500.00 || Find aircraft with lower price than 3000.00
        >>> [aircraft.price_of_flight_in_uan for aircraft in airmovementManagerUtils.find_aircraft_price_lower_than(list_of_aircrafts, 1500.00)]
        [1200.0, 500.0]

        >>> [aircraft.price_of_flight_in_uan for aircraft in airmovementManagerUtils.find_aircraft_price_lower_than(list_of_aircrafts, 3000.00)]
        [2500.0, 1200.0, 500.0]
        """
        result: list = []
        for aircraft in entry_list:
            if aircraft.price_of_flight_in_uan < price_to_compare:
                result.append(aircraft)
        return result

    @staticmethod
    def sort_by_total_capacity_of_passengers(entry_list, sort_type=SortType.ASCENDING):
        """
        #Sorts list of objects by total capacity of passengers with ascending and descending order
        >>> [aircraft.total_capacity_of_passengers for aircraft in airmovementManagerUtils.sort_by_total_capacity_of_passengers(list_of_aircrafts, SortType.ASCENDING)]
        [0, 8, 120]

        >>> [aircraft.total_capacity_of_passengers for aircraft in airmovementManagerUtils.sort_by_total_capacity_of_passengers(list_of_aircrafts, SortType.DESCENDING)]
        [120, 8, 0]
        """
        result: list = []
        if sort_type == SortType.ASCENDING:
            result = sorted(entry_list, key=lambda x: x.total_capacity_of_passengers, reverse=False)
        elif sort_type == SortType.DESCENDING:
            result = sorted(entry_list, key=lambda x: x.total_capacity_of_passengers, reverse=True)
        return result

    @staticmethod
    def sort_by_name_of_aircraft_model(entry_list, sort_type=SortType.ASCENDING):
        """
        Sorts list of objects by name of aircraft model with ascending order && descending order
        >>> [aircraft.name_of_aircraft_model for aircraft in airmovementManagerUtils.sort_by_flight_range_in_km(list_of_aircrafts, SortType.ASCENDING)]
        ['Helicopter', 'Passenger', 'Wizzair']

        >>> [aircraft.name_of_aircraft_model for aircraft in airmovementManagerUtils.sort_by_flight_range_in_km(list_of_aircrafts, SortType.DESCENDING)]
        ['Wizzair', 'Passenger', 'Helicopter']
        """
        result: list = []
        if sort_type == SortType.ASCENDING:
            result = sorted(entry_list, key=lambda x: x.name_of_aircraft_model, reverse=False)
        elif sort_type == SortType.DESCENDING:
            result = sorted(entry_list, key=lambda x: x.name_of_aircraft_model, reverse=True)
        return result

    @staticmethod
    def sort_by_flight_range_in_km(entry_list, sort_type=SortType.ASCENDING):
        """
        Sorts list of objects by flight range in km with ascending order && descending order
        >>> [aircraft.flight_range_in_km for aircraft in airmovementManagerUtils.sort_by_flight_range_in_km(list_of_aircrafts, SortType.ASCENDING)]
        [1000.0, 2500.0, 3000.0]

        >>> [aircraft.flight_range_in_km for aircraft in airmovementManagerUtils.sort_by_flight_range_in_km(list_of_aircrafts, SortType.DESCENDING)]
        [3000.0, 2500.0, 1000.0]
        """
        if sort_type == SortType.ASCENDING:
            return sorted(entry_list, key=lambda x: x.flight_range_in_km, reverse=False)
        elif sort_type == SortType.DESCENDING:
            return sorted(entry_list, key=lambda x: x.flight_range_in_km, reverse=True)


if __name__ == "__main__":
    import doctest

    list_of_aircrafts = [Helicopter(name_of_aircraft_model="Helicopter",
                                    total_capacity_of_passengers=8,
                                    flight_range_in_km=1000.0, price_of_flight_in_uan=2500.0),
                         PassengerAirplane(name_of_aircraft_model="Passenger", total_capacity_of_passengers=120,
                                           flight_range_in_km=2500.0, price_of_flight_in_uan=1200.0),
                         TransportAirplane(name_of_aircraft_model="Wizzair", total_capacity_of_passengers=0,
                                           flight_range_in_km=3000.0, price_of_flight_in_uan=500.0)]
    airmovementManagerUtils = AirmovementManagerUtils()
    doctest.testmod(verbose=True, extraglobs={"obj": AirmovementManagerUtils,
                                              "list_of": list_of_aircrafts})
