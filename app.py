from flask import Flask
from flask_restful import Api, Resource
from flask import Flask, request, jsonify



app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, test):
        return {"name": name, "test": test}


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")


"""
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/ip", methods=["GET"])
def hello():
    msg = "Hello, your IP Address is " + request.remote_addr
    return msg
"""
if __name__ == "__main__":
    app.run(debug=True) # remove "debug=True" if in production environment