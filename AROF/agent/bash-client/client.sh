#!/bin/bash

host_1="10.1.7.65"
host_2="10.1.7.67"
start_url="http://$ipadd/startPlayer"
stop_url="http://$ipadd/stopPlayer"
header1="Accept: application/json"
header2="Content-Type: application/json"
stp="28508ab5-9591-47ed-9445-d5e8e9bafff6"

function post {
        curl --verbose -H \"${header1}\" -H \"${header2}\" -X PUT -d '{\"id\": \"$stp\"}' ${start_url}
}

function get {
        curl -X PUT $stop_url
}

post
get