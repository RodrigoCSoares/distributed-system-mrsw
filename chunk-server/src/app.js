//Constant values
const express = require('express')
const ip = require('ip');
const app = express()
const port = '3000'
const https = require('https')
const request = require('request')

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
            res.send(response.body)
        } else {
            res.send('Chunk server added.')
        }
        console.log('statusCode: ${res.statusCode}')
        console.log(body)
    })
}

app.get('/', (req, res) => connectToDirectory(req, res))
app.listen(port, () => console.log('http://localhost:${port}'))