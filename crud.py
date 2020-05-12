from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from classes.models.aircraft import Aircraft
import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SmartAircraft(Aircraft, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producer_name = db.Column(db.String(32), unique=False)
    name_of_aircraft_model = db.Column(db.String(32), unique=False)
    production_year = db.Column(db.Integer, unique=False)
    total_capacity_of_passengers = db.Column(db.Integer, unique=False)
    tonnage_in_tons = db.Column(db.Float, unique=False)
    type_of_engine = db.Column(db.String(32), unique=False)
    flight_range_in_km = db.Column(db.Float, unique=False)
    price_of_flight_in_uan = db.Column(db.Float, unique=False)

    def __init__(self, producer_name='N/A', name_of_aircraft_model='N/A',
                 production_year=0, total_capacity_of_passengers=0,
                 tonnage_in_tons=0, type_of_engine='N/A', flight_range_in_km=0.0,
                 price_of_flight_in_uan=0.0):
        super().__init__(producer_name, name_of_aircraft_model,
                         production_year, total_capacity_of_passengers,
                         tonnage_in_tons, type_of_engine, flight_range_in_km,
                         price_of_flight_in_uan)


class SmartAircraftSchema(ma.Schema):
    class Meta:
        fields = ('producer_name', 'name_of_aircraft_model',
                  'production_year', 'total_capacity_of_passengers',
                  'tonnage_in_tons', 'type_of_engine', 'flight_range_in_km',
                  'price_of_flight_in_uan')


smart_aircraft_schema = SmartAircraftSchema()
smart_aircrafts_schema = SmartAircraftSchema(many=True)


@app.route("/smart_aircraft", methods=["POST"])
def add_smart_aircraft():
    smart_aircraft = SmartAircraft(request.json['producer_name'],
                                   request.json['name_of_aircraft_model'],
                                   request.json['production_year'],
                                   request.json['total_capacity_of_passengers'],
                                   request.json['tonnage_in_tons'],
                                   request.json['type_of_engine'],
                                   request.json['flight_range_in_km'],
                                   request.json['price_of_flight_in_uan'])
    db.session.add(smart_aircraft)
    db.session.commit()
    return smart_aircraft_schema.jsonify(smart_aircraft)


@app.route("/smart_aircraft", methods=["GET"])
def get_all_smart_aircraft():
    all_smart_aircraft = SmartAircraft.query.all()
    result = smart_aircrafts_schema.dump(all_smart_aircraft)
    return jsonify({'smart_aircrafts': result})


@app.route("/smart_aircraft/<id>", methods=["GET"])
def get_smart_aircraft(id):
    smart_aircraft = SmartAircraft.query.get(id)
    if not smart_aircraft:
        abort(404)
    return smart_aircraft_schema.jsonify(smart_aircraft)


@app.route("/smart_aircraft/<id>", methods=["PUT"])
def update_smart_aircraft(id):
    smart_aircraft = SmartAircraft.query.get(id)
    if not smart_aircraft:
        abort(404)
    old_smart_aircraft = copy.deepcopy(smart_aircraft)
    smart_aircraft.producer_name = request.json['producer_name']
    smart_aircraft.name_of_aircraft_model = request.json['name_of_aircraft_model']
    smart_aircraft.production_year = request.json['production_year']
    smart_aircraft.total_capacity_of_passengers = request.json['total_capacity_of_passengers']
    smart_aircraft.tonnage_in_tons = request.json['tonnage_in_tons']
    smart_aircraft.type_of_engine = request.json['type_of_engine']
    smart_aircraft.flight_range_in_km = request.json['flight_range_in_km']
    smart_aircraft.price_of_flight_in_uan = request.json['price_of_flight_in_uan']
    db.session.commit()
    return smart_aircraft_schema.jsonify(old_smart_aircraft)


@app.route("/smart_aircraft/<id>", methods=["DELETE"])
def delete_smart_aircraft(id):
    smart_aircraft = SmartAircraft.query.get(id)
    if not smart_aircraft:
        abort(404)
    db.session.delete(smart_aircraft)
    db.session.commit()
    return smart_aircraft_schema.jsonify(smart_aircraft)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
