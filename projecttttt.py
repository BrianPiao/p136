from flask import Flask,jsonify,request
from tada import tada

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":tada,
        "message":"success",
    }),200
    
@app.route("/haha")
def planet():
    name = request.args.get("name")
    planetdata = next(item for item in tada if item["name"] == name)
    return jsonify({
        "data":planetdata,
        "message":"success",
    }),200
if __name__ == "__main__":
    app.run(debug = True)