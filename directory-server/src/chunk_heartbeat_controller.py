from flask_restful import Resource, reqparse
from flask import request
import database


# API endpoints
class ChunkHeartBeatController(Resource):

    def post(self, ip):
        post_port = request.headers.get('port')

        for chunkServer in database.chunkServers:
            if ip == chunkServer["ip"] and post_port == chunkServer["port"]:
                print("Beat received from IP: " + ip + ", PORT: " + post_port)
                return "Beat received", 201
        return "Chunk server not registered", 400

