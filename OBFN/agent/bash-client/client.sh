#!/bin/bash

header1="Content-Type:application/json"
header2="Accept:application/json"

function exec_post {
        curl -X POST --header ${header1} --header ${header2} -d '{"operations": [{"x_offset_angle": -90, "y_offset_angle": 90, "beam_id": 0, "wavelength": 1553}, {"x_offset_angle": -90, "y_offset_angle": 90, "beam_id": 1, "wavelength": 1553}, {"x_offset_angle": -90, "y_offset_angle": 90, "beam_id": 2, "wavelength": 1553}, {"x_offset_angle": -90, "y_offset_angle": 90, "beam_id": 3, "wavelength": 1553}]}' 'http://localhost:5002/api/obfn'
}

function exec_get {
        curl -X GET --header ${header2} 'http://localhost:5002/api/obfn'
}

function exec_put {
        curl -X PUT --header ${header1} --header ${header2} 'http://localhost:5002/api/obfn/1?x_offset_angle=-80&y_offset_angle=80&wavelength=1552'
}

function exec_delete {
        curl -X DELETE --header ${header2} 'http://localhost:5002/api/obfn'
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