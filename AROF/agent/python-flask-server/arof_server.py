import argparse
import json

from flask import Flask
from flask import request
from models.arof import Arof
from models.arof_pool import ArofPool

app = Flask(__name__)

mode = ''
spacing = 20
arof_pool = ArofPool()


@app.route('/arof', methods=['GET', 'POST', 'DELETE'])
def arof_root():

    if request.method == 'GET':
        return arof_pool.return_pool()

    if request.method == 'POST':
        for arof in json.loads(request.data.decode('utf-8'))['arof-pool']:
            print(arof)
            arof_id = int(arof['id'])
            if arof_id == 0:
                wavelength = float(arof['wavelength'])
            elif mode == 'incoherent':
                wavelength = float(arof_pool.first_wavelength()+spacing*arof_id)
            else:
                wavelength = float(arof_pool.first_wavelength())
            arof_pool.add(Arof(arof_id=int(arof['id']), wavelength=wavelength, enabled=bool(arof['enabled'])))
        return arof_pool.return_pool()

    if request.method == 'DELETE':
        arof_pool.delete()
        return arof_pool.return_pool()


@app.route('/pause', methods=['GET'])
def pause():
    arof_pool.pause()
    return arof_pool.return_pool()\


@app.route('/resume', methods=['GET'])
def resume():
    arof_pool.resume()
    return arof_pool.return_pool()


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
