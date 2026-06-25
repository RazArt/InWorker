from threading import Thread
from time import sleep
from PIL import ImageGrab

_running = False
_coordinates = {
    'spheres_buff': ((971, 877), (1015, 877), (1059, 877), (1103, 877), (1147, 877), (1191, 877), (1235, 877),
                     (1279, 877), (1323, 877), (1367, 877), (1411, 877), (1455, 877)),
    # 'spheres_buff': ((971, 909), (1015, 909), (1059, 909), (1103, 909), (1147, 909), (1191, 909), (1235, 909),
    #                  (1279, 909), (1323, 909), (1367, 909), (1411, 909), (1455, 909)),
    'spheres': ((767, 945), (825, 945), (883, 945)),
    'spells': ((966, 950), (1024, 950)),
    'other': ((1076, 950), (977, 950), (1035, 950))  #Инвокер, кд на госта, кд на госта 2
}
_pixel_colors = []


def update_info():
    global _pixel_colors

    while _running == True:
        try:
            image = ImageGrab.grab()
            _pixel_colors = []
            for _, group in _coordinates.items():
                for coordinate in group:
                    _pixel_colors.append(image.getpixel(coordinate))
        finally:
            sleep(0.05)


def start():
    global _running
    _running = True

    Thread(target=update_info).start()


def stop():
    global _running
    _running = False


def get_pixel_colors():
    if (_pixel_colors):
        return _pixel_colors
    else:
        return [(0, 0, 0)] * 20
