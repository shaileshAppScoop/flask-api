# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields
from werkzeug.exceptions import BadRequest


# creating a Flask app 
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST'])
def home():
        status = "up"
        return jsonify({'status': status})


# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/square/<int:num>', methods = ['GET'])
def disp(num):
        return jsonify({'data': num**2}), 201


"""
Function returns the dummy matrix in response
"""
@app.route('/product/compatible', methods = ['GET'])
def getCompatibility():
        return jsonify([
            {'id': 1, 'name': 'Product 1', 'shortDescription': 'SD', 'fullDescription': 'FD', 'compatibleProducts':[14,4], 'categoryId':1, 'media':{'id':1,'key':'s3objectkey1', 'url':'https://swagger.io/'}},
            {'id': 2, 'name': 'Product 2', 'shortDescription': 'SD2', 'fullDescription': 'FD2', 'compatibleProducts':[14], 'categoryId':2, 'media':{'id':12,'key':'s3objectkey2', 'url':'https://swagger.io/'}},
            {'id': 14, 'name': 'Product 3', 'shortDescription': 'SD14', 'fullDescription': 'FD14', 'compatibleProducts':[1,2,4], 'categoryId':1},
            {'id': 4, 'name': 'Product 4', 'shortDescription': 'SD4', 'fullDescription': 'FD5', 'compatibleProducts':[1,14], 'categoryId':1, 'media':{'id':3,'key':'s3objectkey3', 'url':'https://swagger.io/'}},
            {'id': 3, 'name': 'Product 45', 'shortDescription': 'DS', 'fullDescription': 'DF', 'compatibleProducts':[], 'categoryId':2, 'media':{'id':44,'key':'s3objectkey4', 'url':'https://swagger.io/'}}
        ])


@app.route('/product/compatible', methods = ['PUT', 'DELETE'])
def alterCompatibility():
        u = request.args.get('productId1')
        v = request.args.get('productId2')
        if u is None or v is None:
                abort(400) # missing arguments or auth header
        return ('', 200)


@app.before_request
def before_request():
        bearer = request.headers.get('Authorization')
        e = BadRequest('No Authorization provided in headers. Attach a valid bearer token.')
        e.data = {'Access': 'Denied', 'CODE': 'Unauthorized'}
        if bearer is None or 'Bearer' not in bearer:
                raise e


@app.after_request
def apply_caching(response):
        response.headers["X-custom-header"] = "custom baat cheet"
        return response


@app.route('/api/users', methods = ['POST'])
def createNewUser():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    return jsonify({ 'username': username, 'password': username  }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}


# driver function 
if __name__ == '__main__':
        app.run(debug = True)
