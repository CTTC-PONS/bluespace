#!/bin/bash

header1="Content-Type:application/json"
header2="Accept:application/json"
hostname="localhost"
port="5002"

function exec_post {
        curl -X POST --header ${header1} --url "http://${hostname}:${port}/api/obfn" \
        --data '{
                "obfn-pool": [
                        {
                                "beam-enable": true,
                                "beam-id": 0,
                                "width": 50,
                                "x-offset-angle": 30,
                                "y-offset-angle": 60
                        },
                        {
                                "beam-enable": true,
                                "beam-id": 1,
                                "width": 51,
                                "x-offset-angle": 31,
                                "y-offset-angle": 61
                        },
                        {
                                "beam-enable": true,
                                "beam-id": 2,
                                "width": 52,
                                "x-offset-angle": 32,
                                "y-offset-angle": 62
                        },
                        {
                                "beam.enable": true,
                                "beam-id": 3,
                                "width": 53,
                                "x-offset-angle": 33,
                                "y-offset-angle": 63
                        }
                ],
                "wavelength-reference-pool": [
                        {
                                "wavelength-id": 0,
                                "central-frequency": 1
                        },
                        {
                                "wavelength-id": 1,
                                "central-frequency": 2
                        },
                        {
                                "wavelength-id": 2,
                                "central-frequency": 3
                        },
                        {
                                "wavelength-id": 3,
                                "central-frequency": 4
                        }
                ]
        }'
}

function exec_get {
        curl -X GET --header ${header2} --url "http://${hostname}:${port}/api/obfn"
}

function exec_put {
        curl -X PUT --header ${header1} --url "http://${hostname}:${port}/api/obfn" \
        --data '{
                "obfn-pool": [
                        {
                                "beam-enable": true,
                                "beam-id": 0,
                                "width": 10,
                                "x-offset-angle": 20,
                                "y-offset-angle": 30
                        }
                ],
                "wavelength-reference-pool": [
                        {
                                "wavelength-id": 0,
                                "central-frequency": 31
                        }
                ]
        }'                
}

function exec_delete {
        curl -X DELETE "http://${hostname}:${port}/api/obfn"
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