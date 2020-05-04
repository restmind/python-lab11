from classes.models.aircraft import Aircraft


class TransportAirplane(Aircraft):
    def __init__(self, producer_name='N/A', name_of_aircraft_model='N/A',
                 production_year=0, total_capacity_of_passengers=0,
                 tonnage_in_tons=0, type_of_engine='N/A', flight_range_in_km=0.0,
                 price_of_flight_in_uan=0.0, delivery_time_in_days=0):
        super().__init__(producer_name, name_of_aircraft_model,
                         production_year, total_capacity_of_passengers,
                         tonnage_in_tons, type_of_engine, flight_range_in_km,
                         price_of_flight_in_uan)
        self._delivery_time_in_days = delivery_time_in_days
