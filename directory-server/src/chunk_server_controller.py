from flask_restful import Resource, reqparse
from flask import request
import database


# API endpoints
class ChunkServerSignInController(Resource):
    def get(self, ip):
        parser = reqparse.RequestParser()
        parser.add_argument("port")
        args = parser.parse_args()

        for chunk_server in database.chunkServers:
            if ip == chunk_server["ip"] and args["port"] == chunk_server["port"]:
                return chunk_server, 200

        return "Chunk server not found", 404

    def post(self, ip):
        post_port = request.headers.get('port')

        for chunkServer in database.chunkServers:
            if ip == chunkServer["ip"] and post_port == chunkServer["port"]:
                return "Chunk server with ip {} and port {} already exists".format(ip, chunkServer["port"]), 400

        new_chunk_server = {
            "ip": ip,
            "port": post_port
        }
        database.chunkServers.append(new_chunk_server)
        return new_chunk_server, 201

    def delete(self, ip):
        parser = reqparse.RequestParser()
        parser.add_argument("port")
        args = parser.parse_args()

        database.chunkServers = [ChunkServer for ChunkServer in database.chunkServers if
                                 ChunkServer["ip"] != ip and ChunkServer["port"] != args["port"]]
        return "Chunk server with ip {} and port {} is deleted.".format(ip, args["port"]), 200
