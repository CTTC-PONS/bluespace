from subprocess import call


class Obfn:
    def __init__(self, arof_id=None, wavelength=None, enabled=None, offset_x=None, offset_y=None, width=None):
        self.obfn_id = int()
        self.wavelength = float()
        self.enabled = bool()
        self.x = int()
        self.y = int()
        self.x = int()

        if arof_id:
            self.obfn_id = arof_id
        if wavelength:
            self.wavelength = wavelength
        if enabled:
            self.enabled = enabled
        if offset_x:
            self.offset_x = offset_x
        if offset_y:
            self.offset_y = offset_y
        if width:
            self.width = width

    def to_json(self):
        return {'id': self.obfn_id, 'wavelength': self.wavelength, 'enabled': self.enabled, 'offset_x': self.offset_x,
                'offset_y': self.offset_y, 'width': self.width}

    def __str__(self):
        return str(self.to_json())

    def is_enabled(self):
        return self.enabled

    def execute(self):
        call_arg_list = ["obfn-conf/obfn-conf", "-v",
                         "-w", "{:f}".format(self.wavelength),
                         "-i", "{:d}".format(self.obfn_id),
                         "-e", "{:d}".format(self.enabled),
                         "-x", "{:f}".format(self.offset_x),
                         "-y", "{:f}".format(self.offset_y),
                         "-z", "{:f}".format(self.width)]
        print('call_arg_list: {}'.format(call_arg_list))
        call(call_arg_list)

    def deactivate(self):
        self.enabled = False

    def activate(self):
        self.enabled = True
