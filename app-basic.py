from flask import Flask
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = restful.Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('name')
# parser.add_argument('age', type=int)
# parser.add_argument('field-with-regex', type=inputs.regex('^[0-9]+$'))
# args = parser.parse_args()

class BlankEndpoints(Resource):
    def get(self):
        return "common response for all endpoints",201
    
    def my_endpoint(self):
        return "custom response from my endpoint"

class EndpointsWithParams(Resource):
    def get(self,params):
        return {'params': params}

# class EndpointWithBody(Resource):
#     def get(self):
#         return {'params': params}

# @api.resource('/foo')
# class EndpointWithInitialAddedRoute(Resource):


#example of endpoint with params
api.add_resource(EndpointsWithParams,'/<string:params>')

#all endpoints will be redirected to this resource
api.add_resource(BlankEndpoints,'/','/nextendpoint','/my-endpoint', endpoint='my_endpoint')

# #endpoints with body
# api.add_resource(EndpointWithBody,'/','/withbody')

# #endpoints with initial route
# api.add_resource(EndpointWithInitialAddedRoute)

if __name__ == '__main__':
    app.run(debug=True)