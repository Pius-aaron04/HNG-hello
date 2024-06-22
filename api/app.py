from flask import jsonify, request
import requests

from api import app

@app.route("/api/hello", strict_slashes=False)
def say_hello():
    visitor = request.args.get("visitor_name").replace('"', '').replace("'", '') or "there"
    headers = request.headers
    if 'X-Forwarded-For' in headers:
        client_ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        client_ip = request.remote_addr
    response = requests.get('http://ipinfo.io/{}/json'.format(client_ip)).json()

    print(client_ip)
    return jsonify({
        "client_ip": response.get('ip'),
        "location": response.get('city'),
        "greeting": "hello {}!".format(visitor)})


if __name__ == '__main__':
    app.run()