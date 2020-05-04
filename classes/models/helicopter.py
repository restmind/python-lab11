from classes.models.aircraft import Aircraft


class Helicopter(Aircraft):
    def __init__(self, producer_name='N/A', name_of_aircraft_model='N/A',
                 production_year=0, total_capacity_of_passengers=0,
                 tonnage_in_tons=0, type_of_engine='N/A', flight_range_in_km=0.0,
                 price_of_flight_in_uan=0.0, quantity_of_screws=0):
        super().__init__(self, producer_name, name_of_aircraft_model,
                         production_year, total_capacity_of_passengers,
                         tonnage_in_tons, type_of_engine, flight_range_in_km,
                         price_of_flight_in_uan)
        self._quantity_of_screws = quantity_of_screws
