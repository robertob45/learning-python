from camera import Camera
from video_camera import VideoCamera

# print('Camera')
print('Video camera')

brand = input('Ingresa marca: ')
sensor = input('Ingresa sensor: ')
sensor = sensor + 'mpx'
lens = input('Ingresa lente: ')
lens = lens + 'mm'
battery = input('Ingresa bateria: ')
battery = battery + 'mAh'
resolution = input('FHD(1), HD(2), o SD(3)?: ')
fps = input('60(1), 30(2), o 24fps?(3): ')
video_save_format = input('MP4(1) o AVI?(2): ')

#flash_use = input('Usar flash s/n?:')
#save_format = input('jpg o raw?: ')

print('')
vcamera_object = VideoCamera(brand, sensor, lens, battery)
print('Usando:', vcamera_object)
print('')
vcamera_object.start_rec(resolution, fps, video_save_format)
