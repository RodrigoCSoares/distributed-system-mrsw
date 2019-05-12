//Global values
var chunk_port
const request = require('request')

//Directory server values
const directoryIp = '127.0.0.1'
const directoryPort = 5000
const directoryEndPoint = "/chunk_server/heartbeat"

//Send heartbeat to directory
function sendBeatToDirectory(req, res) {
    posrUrl = 'http://' + directoryIp + ":" + directoryPort + directoryEndPoint + "/" + directoryIp

    //HTTP post
    request.post(posrUrl, {
        headers: {
            'port': chunk_port
        }
    }, (error, response, body) => {
        if (error) {
            console.error(error)
            return
        }

        //if chunk server not added
        if (response.statusCode == 400) {
            console.error(response.body + ", PORT: " + chunk_port)
        } else {
            console.log('Heartbeat sent.')
        }
        console.log(body)
    })
}

module.exports = {
    beatHeart: function(port) {
        chunk_port = port
        
        setTimeout(function(){
            var heartbeat = require('./heartbeat')
            sendBeatToDirectory()
            heartbeat.beatHeart(chunk_port)
        }, 5000)
    }
}