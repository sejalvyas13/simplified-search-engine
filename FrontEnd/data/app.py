from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/api/info")
def api_info():
    info = {
       "ip" : "127.0.0.1",
       "hostname" : "everest",
       "description" : "Main server",
       "load" : [ 3.21, 7, 14 ]
    }
    return jsonify(info)

app.run()