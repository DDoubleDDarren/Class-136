from flask import Flask,request,jsonify
from code import code

app = Flask(__name__)
@app.route("/")

def index():
    return jsonify({
        "code" : code,
        "message" : "success"
    }),200

@app.route("/planet")

def planet():
    name = request.args.get("name")
    planetdata = next(item for item in code if item["name"] == name)
    return jsonify({
        "code" : planetdata,
        "message" : "success"
    }),200

if __name__ == "__main__":
    app.run()