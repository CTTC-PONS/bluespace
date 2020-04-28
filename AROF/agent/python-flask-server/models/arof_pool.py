import json

from flask import jsonify

wavelength = None

class ArofPool:
    def __init__(self):
        self.arof_pool = {}
        self.paused = []

    def first_wavelength(self):
        return self.arof_pool[0].wavelength

    def add(self, arof):
        print('--arof_pool add--')
        print('\t# arof: {}'.format(arof))
        self.arof_pool[arof.arof_id] = arof

        if arof.enabled:
            self.execute_laser(arof.arof_id)

        if arof.arof_id in self.paused:
            self.paused.remove(arof.arof_id)

        self.resume()

    def return_pool(self):
        print('--arof_pool return_pool--')
        return jsonify([self.arof_pool[arof].to_json() for arof in self.arof_pool])

    def delete(self):
        print('--arof_pool delete--')
        for laser_id in self.arof_pool:
            if self.arof_pool[laser_id].is_enabled():
                self.deactivate_laser(laser_id)
                self.execute_laser(laser_id)
            if laser_id in self.paused:
                self.paused.remove(laser_id)

        self.arof_pool = {}

    def pause(self):
        print('--arof_pool pause--')
        for laser_id in self.arof_pool:
            if self.arof_pool[laser_id].is_enabled():
                self.pause_laser(laser_id)
                self.deactivate_laser(laser_id)
                self.execute_laser(laser_id)

    def resume(self):
        print('--arof_pool resume--')
        if self.paused:
            for arof_id in self.paused:
                self.activate_laser(arof_id)
                self.execute_laser(arof_id)
            self.paused = []

    def pause_laser(self, laser_id):
        self.paused.append(laser_id)

    def activate_laser(self, laser_id):
        self.arof_pool[laser_id].activate()

    def deactivate_laser(self, laser_id):
        self.arof_pool[laser_id].deactivate()

    def execute_laser(self, laser_id):
        self.arof_pool[laser_id].execute()


    def cont(self):
        print('--arof_pool cont--')
        for laser_id in self.paused:
            self.activate_laser(laser_id)
        self.paused = []
