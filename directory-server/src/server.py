from flask import Flask
from flask_restful import Api, Resource, reqparse

# Create the application instance
app = Flask(__name__)
api = Api(app)

# Create the database
users = [
    {
        "name": "Rodrigo",
        "age": 19,
        "occupation": "Software Engineer"
    },
    {
        "name": "Angel",
        "age": 32,
        "occupation": "Singer"
    },
    {
        "name": "Jessica",
        "age": 43,
        "occupation": "Developer"
    }
]


# API endpoints
class User(Resource):
    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
            return "User not found", 404

    def post(sel, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                return "User with {} already exists".format(name), 400

            user = {
                "name": name,
                "age": args["age"],
                "occupation": args["occupation"]
            }
            users.append(user)
            return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


# Add api resource route
api.add_resource(User, "/user/<string:name>")
app.run(debug=True)
