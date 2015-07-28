#from marshmallow import Schema, fields
import marshmallow as ma
from flask_marshmallow import Marshmallow, Schema

#models
class SwiftUser:
    """
    Service model for SwiftUser
    """
    
    userid = None
    username = None
    email = None
    
class SwiftUsersCollection():
    def __init__(self, _users):
        self.users = _users
       
#marshmallow schemas 
class SwiftUserSchema(Schema):
    pass
    class Meta:
        fields = ("userid", "username", "email")
        
class SwiftUsersCollectionSchema(Schema):
    users = ma.fields.Nested(SwiftUserSchema, many=True)