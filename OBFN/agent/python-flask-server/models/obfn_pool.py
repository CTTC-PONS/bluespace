import json

from flask import jsonify


class ObfnPool:
    def __init__(self):
        self.obfn_pool = {}

    def first_wavelength(self):
        return self.obfn_pool[0].wavelength

    def add(self, arof):
        print('--obfn_pool add--')
        print('\t# arof: {}'.format(arof))
        self.obfn_pool[arof.obfn_id] = arof
        self.execute_laser(arof.obfn_id)

    def return_pool(self):
        print('--obfn_pool return_pool--')
        return jsonify([self.obfn_pool[arof].to_json() for arof in self.obfn_pool])

    def delete(self):
        print('--obfn_pool delete--')
        for laser_id in self.obfn_pool:
            if self.obfn_pool[laser_id].is_enabled():
                self.deactivate_laser(laser_id)
                self.execute_laser(laser_id)

        self.obfn_pool = {}


    def activate_laser(self, laser_id):
        self.obfn_pool[laser_id].activate()

    def deactivate_laser(self, laser_id):
        self.obfn_pool[laser_id].deactivate()

    def execute_laser(self, laser_id):
        self.obfn_pool[laser_id].execute()

    def cont(self):
        print('--obfn_pool cont--')
        for laser_id in self.paused:
            self.activate_laser(laser_id)
        self.paused = []
