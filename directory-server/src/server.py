from flask import Flask
from flask_restful import Api
from chunk_server_controller import ChunkServerSignInController
from client_controller import ClientController


# Create the application instance
app = Flask(__name__)
api = Api(app)
chunk_controller = ChunkServerSignInController
client_controller = ClientController

# Add api resource route
api.add_resource(chunk_controller, "/chunk_server/<string:ip>")
api.add_resource(client_controller, "/client/<string:data>")
app.run(debug=True)
