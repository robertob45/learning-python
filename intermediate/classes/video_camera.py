from camera import Camera

class VideoCamera(Camera):
    """docstring for ."""
    def __init__(self, brand, sensor, lens, battery):
        super().__init__(brand, sensor, lens, battery)

    def fps(self, fps):
        if fps == '1':
            print('Recording at: 60FPS')
        elif fps == '2':
            print('Recording at: 30FPS')
        elif fps == '3':
            print('Recording at: 24FPS')
        else:
            print('Invalid fps rate, recording at default (30FPS)')


    def resolution(self, resolution):
        if resolution == '1':
            print('Recording in: FHD')
        elif resolution == '2':
            print('Recording in: HD')
        elif resolution == '3':
            print('Recording in: SD')
        else:
            print('Invalid resolution, recording in default (HD)')

    def vsave_format(self, video_save_format):
        if video_save_format == '1':
            print('Saving in: MP4')
        elif video_save_format == '2':
            print('Saving in: AVI')
        else:
            print('Invalid save format, Saving in default (MP4)')

    def start_rec(self, resolution, fps, video_save_format):
        self.frame()
        self.focus()
        self.resolution(resolution)
        self.fps(fps)
        self.vsave_format(video_save_format)
        print('')
        print('Recording...')
