from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from swift_service_models import SwiftUser, SwiftUsersCollection, SwiftUsersCollectionSchema
from flask_marshmallow import Marshmallow
   
#configuraton  
DEBUG = True
SECRET_KEY = 'skainDevKey'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
ma = Marshmallow(app)

#helpers

    
usersCollection_schema = SwiftUsersCollectionSchema()

#routes
@app.route('/')
def show_index():
    return render_template('index.html')
    
@app.route('/users', methods=['GET'])
def get_users():    
    user1 = SwiftUser()
    user1.userid = 1
    user1.username = 'john'
    user1.email = 'john@swift.com' 
    
    user2 = SwiftUser()
    user2.userid = 2
    user2.username = 'jim'
    user2.email = 'jim@swift.com'
    
    coll = SwiftUsersCollection([user1, user2])
    return usersCollection_schema.jsonify(coll)
    # schema = UsersSchema()
    # result,errors = schema.dump(coll)
    # pprint(result)
    # return jsonify(users=[
    #     {
    #         'id': 1,
    #         'username': 'jim',
    #         'email': 'jim@swift.com'
    #     },
    #     {
    #         'id': 2,
    #         'username': 'bones',
    #         'email': 'bones@swift.com'
    #     }
    # ]);

@app.route('/users', methods=['POST']) #probably don't want to implement this one...
def create_user():
    return jsonify({
        'id': 3,
        'username': 'paul',
        'email': 'pual@swift.com'
      #  'username': request.form['username'],
      #  'email': request.form['email']
    })
    
@app.route('/users/<userid>', methods=['GET'])
def get_user():
    pass

@app.route('/users/<userid>', methods=['PUT'])
def update_user():
    pass
    
@app.route('/users/<userid>', methods=['DEL'])
def delete_user():
    pass
    
#main
if __name__ == '__main__':
    app.run()