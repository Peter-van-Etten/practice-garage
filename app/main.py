# flake8: noqa
import os
_credentials = None
_project = None
debug = os.environ.get('FLASK_ENV', 'prod') == 'development'
if debug:
    os.environ["DATASTORE_DATASET"] = "test"
    os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8000"
    os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "localhost:8000/datastore"
    os.environ["DATASTORE_HOST"] = "http://localhost:8000"
    os.environ["DATASTORE_PROJECT_ID"] = "test"
    print('setting mock credentials')
    _project = 'test'
    import mock
    from google.auth import credentials
    _credentials = mock.Mock(spec=credentials.Credentials)

from flask import Flask, render_template, jsonify, request

from shared.system import datastore
from shared.model.car import Car
from shared.model.garage import Garage
from google.cloud import ndb
from app.handlers import garages
from app.handlers import cars

app = Flask(__name__)
app.register_blueprint(garages.bp)
app.register_blueprint(cars.bp)

@app.route('/health-check')
def root():
    return 'Ok'

@app.route('/')
def testing():
    return render_template('index.html')

@app.route('/test-create')
def test_create():
    with datastore.client.context():
        g = Garage(name='vigo', brand='opel', postal_country='NL')
        g.put()
        garages = [g for g in Garage.query()]
        return jsonify([{'name': g.name} for g in garages])

@app.route('/test')
def test_list():
    with datastore.client.context():
        garages = [g for g in Garage.query()]
        return jsonify([{'name': g.name} for g in garages])

@app.route('/create-cars')
def create_cars():
    for g in Garage.list():
        car = Car(garage=g.key, brand=g.brand, license_plate="abcd123")
        car.save()
    return 'OK'

@app.route('/carlist')
def list_cars():
    garages = [c.garage for c in Car.list()]
    # with Car.ndb_context():
    garages = ndb.get_multi(garages)
    for g in garages:
        print(g.name)
    for c in Car.list():
        print(c.garage.get().name)

    return 'OK'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
