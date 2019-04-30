#!/usr/bin/env python3
import logging
import connexion

from logging.handlers import RotatingFileHandler
from swagger_server import encoder

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.DEBUG)


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'OBFN API'})
    fileHandler = RotatingFileHandler('python_flask_server.log', maxBytes=1000000, backupCount=5)
    streamHandler = logging.StreamHandler()
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    app.run(port=5002)


if __name__ == '__main__':
    main()
