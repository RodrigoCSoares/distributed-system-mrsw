from flask_restful import Resource, reqparse
from flask import request
import database
import asyncio
import time
import requests


async def beat():
    max_time_of_gaps = 10
    database.beat_controller_running = True
    while True:
        current_time = time.time()
        for chunkServer in database.chunkServers:
            if current_time - chunkServer["last_heart_beat"] > max_time_of_gaps:
                print("Chunk server dead, IP:" + chunkServer["ip"] + ", PORT:" + chunkServer["port"])
                database.chunkServers.remove(chunkServer)
                clone_data_into_other_chunks(chunkServer)

        await asyncio.sleep(5)


def clone_data_into_other_chunks(chunk_server):
    for data in chunk_server["data"]:
        for chunk_server in database.chunkServers:
            if chunk_server["data"].count(data) == 0:
                chunk_server["data"].append(data)
                headers = {"data": data}
                requests.post('http://' + chunk_server['ip'] + ':' + chunk_server['port'] + '/post_data'
                              , headers=headers)


# API endpoints
class ChunkHeartBeatController(Resource):

    def __init__(self):
        if not database.beat_controller_running:
            asyncio.run(beat())

    def post(self, ip):
        post_port = request.headers.get('port')

        for chunkServer in database.chunkServers:
            if ip == chunkServer["ip"] and post_port == chunkServer["port"]:
                print("Beat received from IP: " + ip + ", PORT: " + post_port)
                chunkServer["last_heart_beat"] = time.time()
                return "Beat received", 201
        return "Chunk server not registered", 400
