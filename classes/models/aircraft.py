class Aircraft:
    def __init__(self, producer_name='N/A', name_of_aircraft_model='N/A',
                 production_year=0, total_capacity_of_passengers=0,
                 tonnage_in_tons=0, type_of_engine='N/A', flight_range_in_km=0.0,
                 price_of_flight_in_uan=0.0):
        self.producer_name = producer_name
        self.name_of_aircraft_model = name_of_aircraft_model
        self.production_year = production_year
        self.total_capacity_of_passengers = total_capacity_of_passengers
        self.tonnage_in_tons = tonnage_in_tons
        self.type_of_engine = type_of_engine
        self.flight_range_in_km = flight_range_in_km
        self.price_of_flight_in_uan = price_of_flight_in_uan

    def __str__(self):
        return "Producer name: {}\n" \
               "Name of aircraft model: {}\n" \
               "Production year: {}\n" \
               "Total capacity of passengers: {}\n" \
               "Tonnage in tons: {}\n" \
               "Type of engine: {}\n" \
               "Flight range in km: {}\n" \
               "price of flight in uan: {}\n".format(self._producer_name, self._name_of_aircraft_model,
                                                     self._production_year, self._total_capacity_of_passengers,
                                                     self._tonnage_in_tons, self._type_of_engine,
                                                     self._flight_range_in_km, self._price_of_flight_in_uan)

    def take_off(self):
        print("The plane " + self._name_of_aircraft_model + " is taking off.")

    def land(self):
        print("The plane " + self._name_of_aircraft_model + " is landing.")
