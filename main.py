from flask import Flask, request, jsonify

app = Flask(__name__)

from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/", methods=["GET"])
def home():
    print(request.remote_addr)
    return "The Firewall has been breached" 

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 201

@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    #if request.method == "POST"     returns true or false
    data = request.get_json()
    
    print(request.remote_addr)
    
    print(data)
    
    return jsonify(data), 201
    

#GET Request data from specified resource
#POST Create a resource
#PUT Update a resource
#DELETE Delete a resource


if __name__ == "__main__":
    app.run(debug=True)