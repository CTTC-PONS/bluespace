#!/bin/bash

header1="Content-Type:application/json"
header2="Accept:application/json"
hostname="192.168.1.94"
port="5001"

function exec_post {
        curl -X POST --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/0?enable=false"
        curl -X POST --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/1?enable=false"
        curl -X POST --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/2?enable=false"
        curl -X POST --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/3?enable=false"
}

function exec_get {
        curl -X GET --header ${header2} "http://${hostname}:${port}/api/arof"
}

function exec_put {

        curl -X PUT --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/0?enable=true"
        curl -X PUT --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/1?enable=true"
        curl -X PUT --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/2?enable=true"
        curl -X PUT --header ${header1} --header ${header2} "http://${hostname}:${port}/api/arof/3?enable=true"
}

function exec_delete {
        curl -X DELETE --header ${header2} "http://${hostname}:${port}/api/arof/0"
        curl -X DELETE --header ${header2} "http://${hostname}:${port}/api/arof/1"
        curl -X DELETE --header ${header2} "http://${hostname}:${port}/api/arof/2"
        curl -X DELETE --header ${header2} "http://${hostname}:${port}/api/arof/3"
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