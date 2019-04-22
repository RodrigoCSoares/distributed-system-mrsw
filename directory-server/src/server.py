from flask import Flask
from flask_restful import Api
from chunk_server import ChunkServer

# Create the application instance
app = Flask(__name__)
api = Api(app)
chunk = ChunkServer

# Add api resource route
api.add_resource(chunk, "/chunk_server/<string:ip>")
app.run(debug=True)
