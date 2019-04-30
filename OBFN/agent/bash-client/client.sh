#!/bin/bash

header1="Content-Type:application/json"
header2="Accept:application/json"

function exec_post {
        curl -X POST --header ${header1} --header ${header2} -d '[{"X_offset_angle": -90, "Y_offset_angle": 90, "beam_id": 1 }, {"X_offset_angle": -90, "Y_offset_angle": 90, "beam_id": 2 }, {"X_offset_angle": -90, "Y_offset_angle": 90, "beam_id": 3}, {"X_offset_angle": -90, "Y_offset_angle": 90, "beam_id": 4}]' 'http://10.1.7.64:5002/api/obfn'
}

function exec_get {
        curl -X GET --header ${header2} 'http://10.1.7.64:5002/api/obfn'
}

function exec_put {
        curl -X PUT --header ${header1} --header ${header2} 'http://10.1.7.64:5002/api/obfn/1?X_offset_angle=-80&Y_offset_angle=80'
}

function exec_delete {
        curl -X DELETE --header ${header2} 'http://10.1.7.64:5002/api/obfn'
}

echo "POST"
exec_post
echo "GET"
exec_get
echo "MODIFY BEAM with beam_id = 1"
exec_put
echo "GET"
exec_get
echo "DELETE"
exec_delete