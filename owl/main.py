from owlready2 import *
from flask import Flask, request, jsonify

app = Flask(__name__)
onto = get_ontology("navy_docking.owl")
onto.load()

from random import randint

from json import JSONEncoder
class DockEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__    

docks = []
def generate_docks(n):
    with onto:
        for _ in range(n):
            dock = onto.Dock()
            dock.VelocityWind = randint(0, 25)
            dock.VelocityCurrent = randint(0, 3)
            docks.append(dock)


@app.route("/")
@app.route("/docks/")
def get_docks():
    print(docks)
    return jsonify([{
        'Id': id(dock),
        'VelocityWind': dock.VelocityWind,
        'VelocityCurrent': dock.VelocityCurrent,
    } for dock in docks])


@app.route("/docks/{id}/")
def get_dock(id):
    print(id)
    return jsonify([{
        'Id': id(dock),
        'VelocityWind': dock.VelocityWind,
        'VelocityCurrent': dock.VelocityCurrent,
    } for dock in docks])

@app.route("/docks/available/")
def get_available_dock():
    for dock in docks:
        if dock.VelocityWind < 20 and dock.VelocityCurrent < 2:
            return jsonify({
                'Id': id(dock),
                'VelocityWind': dock.VelocityWind,
                'VelocityCurrent': dock.VelocityCurrent,
            })
    
generate_docks(7)
app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5000)       
