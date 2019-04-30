#!/bin/bash

header1="Content-Type:application/json"
header2="Accept:application/json"

function exec_post {
        curl -X POST --header ${header1} --header ${header2} 'http://localhost:5001/api/arof/1?enable=false'
        curl -X POST --header ${header1} --header ${header2} 'http://localhost:5001/api/arof/2?enable=false'
        curl -X POST --header ${header1} --header ${header2} 'http://localhost:5001/api/arof/3?enable=false'
        curl -X POST --header ${header1} --header ${header2} 'http://localhost:5001/api/arof/4?enable=false'
}

function exec_get {
        curl -X GET --header ${header2} 'http://localhost:5001/api/arof'
}

function exec_put {

        curl -X PUT --header ${header1} --header ${header2} 'http://localhost:5001/api/arof/1?enable=true'
        curl -X PUT --header ${header1} --header ${header2} 'http://localhost:5001/api/arof/2?enable=true'
        curl -X PUT --header ${header1} --header ${header2} 'http://localhost:5001/api/arof/3?enable=true'
        curl -X PUT --header ${header1} --header ${header2} 'http://localhost:5001/api/arof/4?enable=true'
}

function exec_delete {
        curl -X DELETE --header ${header2} 'http://localhost:5001/api/arof/1'
        curl -X DELETE --header ${header2} 'http://localhost:5001/api/arof/2'
        curl -X DELETE --header ${header2} 'http://localhost:5001/api/arof/3'
        curl -X DELETE --header ${header2} 'http://localhost:5001/api/arof/4'
}

echo "ENSURE LASERS OFF"
exec_post
echo "ENABLE LASERS"
exec_put
echo "GET OPERATIONS ON LASERS"
exec_get
echo "DISABLE LASERS"
exec_delete
exec_get