from flask import Flask, request, jsonify
from flask_cors import CORS
from rrt import *
import json
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def hello():
    content = request.json
    startpos = (content["startpos"]["lat"], content["startpos"]["lng"])
    endpos = (content["endpos"]["lat"], content["endpos"]["lng"])
    positions = content["positions"]
    print startpos, endpos, positions

    #obstacles = [(p[0], p[1]) for p in positions]
    obstacles []
    n_iter = 200
    radius = 0.01
    stepSize = 0.01

    print obstacles

    G = RRT_star(startpos, endpos, obstacles, n_iter, radius, stepSize)

    print(G.success)
    if G.success:
        path = dijkstra(G)
        p = [{"x": node[0], "y": node[1]} for node in path]
        data = jsonify({'path': p})
        return data
    else:
        return jsonify({'path': []})
