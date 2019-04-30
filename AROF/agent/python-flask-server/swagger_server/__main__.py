#!/usr/bin/env python3
import logging
from logging.handlers import RotatingFileHandler

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'AROF API'})
    handler = RotatingFileHandler('python-flask-server.log', maxBytes=1000000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    app.run(port=5001)


if __name__ == '__main__':
    main()
