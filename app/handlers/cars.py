from flask import Blueprint, abort, jsonify, request
from shared.model.garage import Garage
from shared.model.car import Car
import logging

bp = Blueprint(name='cars', import_name=__name__, url_prefix='/cars')

@bp.route('/cars-from-garage/<int:garage_id>', methods=["GET"])
def cars_from_garage(garage_id):
    garage = Garage.get(garage_id)
    cars = Car.list(garage=garage)
    return jsonify(
        [
            {
                'id': car.id,
                'brand': car.brand,
                'license_plate': car.license_plate
            } for car in cars
        ]
    )

@bp.route('/', methods=["POST"])
def car_add():
    # print('car_add:', request.json)
    garage_id = request.json.pop('garage_id')
    garage = Garage.get(garage_id)
    Car.add(props=request.json, garage=garage.key)
    return cars_from_garage(garage_id)

@bp.route('/', methods=["PUT"])
def car_update():
    # print('car_update:', request.json)
    props = request.json
    car = Car.get(key=props.pop("id"))
    garage_id = car.garage.id
    car.update(props=props)
    return cars_from_garage(garage_id)

@bp.route('/', methods=["DELETE"])
def car_delete():
    # print('car_delete:', request.json)
    car = Car.get(key=request.json.pop("car"))
    garage_id = car.garage.id
    car.delete()
    return cars_from_garage(garage_id)
