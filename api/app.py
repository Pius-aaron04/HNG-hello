from flask import jsonify, request
import requests

from api import app

@app.route("/api/hello", strict_slashes=False)
def say_hello():
    visitor = request.args.get("visitor_name") or "there"
    client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    response = requests.get('http://ipinfo.io/{}/json'.format(client_ip)).json()

    return jsonify({
        "client_ip": response.get('ip'),
        "location": response.get('city'),
        "greeting": "hello {}!".format(visitor)})


if __name__ == '__main__':
    app.run()