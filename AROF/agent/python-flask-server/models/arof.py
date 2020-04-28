class Arof:
    def __init__(self, arof_id=None, wavelength=None, enabled=None):
        self.arof_id = int()
        self.wavelength = float()
        self.enabled = bool()

        if arof_id:
            self.arof_id = arof_id
        if wavelength:
            self.wavelength = wavelength
        if enabled:
            self.enabled = enabled

    def to_json(self):
        return {'id': self.arof_id, 'wavelength': self.wavelength, 'enabled': self.enabled}

    def __str__(self):
        return str(self.to_json())

    def is_enabled(self):
        return self.enabled

    def execute(self):
        call_arg_list = ["arof-conf/arof-conf", "-v",
                         "-i", "{:d}".format(self.arof_id),
                         "-e", "{:d}".format(self.enabled),
                         "-w", "{:f}".format(self.wavelength)]
        print('call_arg_list: {}'.format(call_arg_list))
        # call(call_arg_list)

    def deactivate(self):
        self.enabled = False

    def activate(self):
        self.enabled = True
