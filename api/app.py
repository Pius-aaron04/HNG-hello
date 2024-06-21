from flask import jsonify, request
import requests

from api import app

@app.route("/api/hello", strict_slashes=False)
def say_hello():
    visitor = request.args.get("visitor_name") or "there"
    
    response = requests.get('http://ipinfo.io/{}/json'.format(request.remote_addr)).json()

    return jsonify({
        "client_ip": response.get('ip_address'),
        "location": response.get('country__name'),
        "greeting": "hello {}!".format(visitor)})


if __name__ == '__main__':
    app.run()