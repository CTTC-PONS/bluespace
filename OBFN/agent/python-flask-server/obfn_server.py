import argparse
import json

from flask import Flask
from flask import request
from models.obfn import Obfn
from models.obfn_pool import ObfnPool

app = Flask(__name__)

mode = ''
obfn_pool = ObfnPool()
spacing = 20

@app.route('/obfn', methods=['GET', 'POST', 'DELETE'])
def obfn_root():

    if request.method == 'GET':
        return obfn_pool.return_pool()

    if request.method == 'POST':
        for obfn in json.loads(request.data.decode('utf-8'))['obfn-pool']:
            obfn_id = int(obfn['beam-id'])
            if obfn_id == 0:
                wavelength_pool = json.loads(request.data.decode('utf-8'))['wavelength-reference-pool']
                wavelength = float(wavelength_pool[0]['central-frequency'])
            elif mode == 'incoherent':
                wavelength = float(obfn_pool.first_wavelength() + spacing * obfn_id)
            else:
                wavelength = float(obfn_pool.first_wavelength())

            obfn_pool.add(Obfn(
                arof_id=int(obfn['beam-id']),
                wavelength=wavelength,
                enabled=bool(obfn['beam-enable']),
                offset_x=int(obfn['x-offset-angle']),
                offset_y=int(obfn['y-offset-angle']),
                width=int(obfn['width'])
            ))
        return obfn_pool.return_pool()

    if request.method == 'DELETE':
        obfn_pool.delete()
        return obfn_pool.return_pool()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ARoF agent (port, mode)')
    parser.add_argument('--port', '-p')
    parser.add_argument('--mode', '-m')
    parser.add_argument('--spacing', '-s')

    args = parser.parse_args()
    mode = str(args.mode)
    if args.spacing:
        spacing = float(args.spacing)

    print(args.__dict__)

    app.run(host='0.0.0.0', port=int(args.port))
