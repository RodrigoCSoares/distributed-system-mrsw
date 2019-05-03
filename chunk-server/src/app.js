//Constant values
const express = require('express')
const ip = require('ip');
const readline = require('readline');
const app = express()
const https = require('https')
const request = require('request')
var heartbeat = require('./heartbeat')
var port

//Directory server values
const directoryIp = '127.0.0.1'
const directoryPort = 5000
const directoryEndPoint = "/chunk_server"

//Function to connect to directory sending a HTTP POST
function connectToDirectory(req, res) {
    posrUrl = 'http://' + directoryIp + ":" + directoryPort + directoryEndPoint + "/" + directoryIp

    //HTTP post
    request.post(posrUrl, {
        headers: {
            'port': port
        }
    }, (error, response, body) => {
        if (error) {
            console.error(error)
            return
        }

        //if chunk server already added
        if (response.statusCode == 400) {
            console.error(response.body)
        } else {
            console.log('Chunk server added.')
        }
        console.log(body)
    })
}

//Function to save directory'ponto e virgula em ingless data
function saveDirectorysData(req, res) {
    console.log("Post received: " + req.get("data"))
    res.end("data received")
}

//Request the server's port to the user
function requestPort() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
      });
      
      rl.question('What port does server should use? ', (answer) => {
        port = answer  
        console.log(`Port: ${answer}`);
        configServer()
        rl.close();
      });
}

function configServer(){
    connectToDirectory()
    app.post('/post_data', (req, res) => saveDirectorysData(req, res))
    app.listen(port, () => console.log('http://localhost:' + port))
    heartbeat.beatHeart(port)
}

requestPort()