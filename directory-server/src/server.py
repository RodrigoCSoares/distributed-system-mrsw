from flask import Flask
from flask_restful import Api
from chunk_server_controller import ChunkServerSignInController
from client_controller import ClientController
from chunk_heartbeat_controller import ChunkHeartBeatController


# Create the application instance
app = Flask(__name__)
api = Api(app)
chunk_controller = ChunkServerSignInController
client_controller = ClientController
chunks_heartbeat_controller = ChunkHeartBeatController

# Add api resource route
api.add_resource(chunk_controller, "/chunk_server/<string:ip>")
api.add_resource(client_controller, "/client/<string:data>")
api.add_resource(chunks_heartbeat_controller, "/chunk_server/heartbeat/<string:ip>")
app.run(debug=True)
