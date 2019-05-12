import requests
from flask_restful import Resource, reqparse
import database


class ClientController(Resource):
    def get(self, data):
        return

    def post(self, data):
        if len(database.chunkServers) == 0:
            return "Service unavailable", 503

        headers = {"data": data}
        for chunk_server in database.chunkServers:
            chunk_server["data"].append(data)
            requests.post('http://' + chunk_server['ip'] + ':' + chunk_server['port'] + '/post_data', headers=headers)

        return "Data sent", 201

    def delete(self, data):
        return
