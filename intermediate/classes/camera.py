class Camera:
    """docstring for ."""
    def __init__(self, brand, sensor, lens, battery):
        self.brand = brand
        self.sensor = sensor
        self.lens = lens
        self.battery = battery

    def __str__(self):
        return self.brand + ' ' + self.sensor + ' ' + self.lens + ' ' + self.battery

    def focus(self):
        print('Focusing using', self.lens, '...')
        print('')

    def frame(self):
        print('Move until your subject is in the desired position')
        print('.')
        print('.')
        print('.')

    def flash(self, flash_use):
        if flash_use == 's':
            print('Shooting with flash...')
        else:
            print('Shooting without flash...')
        print('')

    def format(self, save_format):
        if save_format == 'jpg':
            print('Saving in: ' + save_format)
        elif save_format == 'raw':
            print('Saving in: ' + save_format)
        else:
            print('No valid format to save')

    def take_picture(self, save_format, flash_use):
        print('Say cheese!')
        self.focus()
        self.frame()
        self.flash(flash_use)
        self.format(save_format)
