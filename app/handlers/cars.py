from flask import Blueprint, abort, jsonify, request
from shared.model.garage import Garage
from shared.model.car import Car
import logging

bp = Blueprint(name='cars', import_name=__name__, url_prefix='/garages/carlist')

# @garages.route('/', defaults={'page': 'index'})
@bp.route('/', methods=["GET"])
def car_list():
    print(request.args)
    if request.args and 'car' in request.args:
        car = car.get(key=request.args.get('car'))
        return jsonify({
            'id': car.id,
            'garage': car.garage,
            'brand': car.brand,
            'license_plate': car.license_plate
        })
    return jsonify(
        [
            {
                'id': g.id,
                'garage': g.garage,
                'brand': g.brand,
                'license_plate': g.license_plate
            } for g in Car.list()
        ]
    )


@bp.route('/', methods=["POST"])
def car_add():

    car = Car.add(props=request.json)
    return car_list()

@bp.route('/', methods=["PUT"])
def car_update():
    props = request.json
    car = Car.get(key=props.pop('id'))
    car.update(props=props)
    return car_list()

@bp.route('/', methods=["DELETE"])
def car_delete():
    car = Car.get(key=request.json.pop('car'))
    car.delete()
    return car_list()
