import threading
import time
import math

import cv2
import numpy
from ffpyplayer.player import MediaPlayer
from PIL import Image


def _fix_metadata(metadata:dict):
    return {'src_video_size': metadata['src_vid_size'], 
            'title': metadata['title'][2 : -1], 
            'duration': int(metadata['duration']),
            'frame_rate': (lambda x: math.ceil(x[0] / (x[1] + 1)))(metadata['frame_rate']),
            'src_pix_fmt': str(metadata['src_pix_fmt'])[2 : -1],
            'aspect_ratio': metadata['aspect_ratio']}

class VideoPlayer:
    def __init__(self, filename, paused=False, fullscreen=False, key_controls=True, skip_interval=5, blocking=False):
        opts = {'sync': 'audio', 'autoexit': True, 'paused': paused}
        self.player = MediaPlayer(filename, ff_opts=opts)
        time.sleep(1)
        self.pause = self.player.get_pause()
        self.fullscreen = fullscreen
        self.skip_interval = skip_interval
        self.key_controls = key_controls
        self.state = None
        self.frame = None
        try:
            handler_thread = threading.Thread(target=self.player_handler, args=(filename, ), daemon=True)
            if blocking:
                handler_thread.run()
            else:
                handler_thread.start()
        except Exception:
            print('cvplayer::error: unable to initialize player')

    def player_handler(self, filename):
        opts = {'sync': 'audio', 'autoexit': True, 'paused': True}
        if self.pause:
            self.state = 'paused'
            cv2.imshow('video', numpy.zeros((512, 512, 3), dtype = "uint8"))
            pressed_key = cv2.waitKey(0) & 0xFF
            if pressed_key != 255:  print(pressed_key)
            if pressed_key == ord(' ') or pressed_key == ord('k') or pressed_key == ord('K'):
                self.pause = False
                self.player.toggle_pause()
        while True:
            cv2.namedWindow('video', cv2.WINDOW_KEEPRATIO)
            frame, val = self.player.get_frame()
            if val != 'eof':
                if int(self.player.get_pts()) == int(self.player.get_metadata()['duration']):
                    time.sleep(val)
                    self.state = 'eof'
                    self.player.close_player()
                    self.player = MediaPlayer(filename, ff_opts=opts)
                    break
                if isinstance(val, str):
                    waitkey = 32
                elif int(val) == 0:
                    waitkey = 32
                else:
                    waitkey = int(val * 100)
                pressed_key = cv2.waitKey(waitkey) & 0xFF
                if self.key_controls and pressed_key != 255:
                    if pressed_key == ord('q') or pressed_key == 81 or pressed_key == 27:
                        self.player.close_player()
                        self.state = 'eof'
                        break
                    elif pressed_key == ord(' ') or pressed_key == ord('k') or pressed_key == ord('K'):
                        self.pause = not self.pause
                        self.player.toggle_pause()
                        if self.player.get_pause():
                            self.state = 'paused'
                        else:
                            self.state = 'playing'
                    elif pressed_key == ord('r') or pressed_key == ord('R'):
                        self.player.seek(0, relative=False)
                        self.player.get_frame()
                    elif pressed_key == ord('l') or pressed_key == ord('L'):
                        self.player.seek(self.skip_interval, relative=True, accurate=False)
                        self.player.get_frame()
                    elif pressed_key == ord('j') or pressed_key == ord('J'):
                        self.player.seek(-self.skip_interval, relative=True, accurate=False)
                        self.player.get_frame()
                    elif pressed_key == ord('f') or pressed_key == ord('F'):
                        self.fullscreen = not self.fullscreen
                    elif pressed_key == ord('i') or pressed_key == ord('I'):
                        self.player.set_volume(self.player.get_volume() + 0.1)
                    elif pressed_key == ord('o') or pressed_key == ord('O'):
                        self.player.set_volume(self.player.get_volume() - 0.1)

                if not self.pause:
                    self.state = 'playing'
                    if frame is not None:
                        image, pts = frame
                        self.frame = image
                        x, y = image.get_size()
                    else:
                        x, y = '', ''

                    if val != 'eof' or frame is not None:
                        if self.fullscreen is True:
                            cv2.setWindowProperty(
                                'video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                        elif self.fullscreen is False:
                            if x != '' and y != '':
                                cv2.resizeWindow('video', x, y)
                            cv2.setWindowProperty(
                                'video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
                        if frame is not None:
                            x, y = image.get_size()
                            data = image.to_bytearray()[0]
                            image =  Image.frombytes("RGB", (x, y), bytes(data))
                            image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
                            cv2.imshow('video', image)
                    else:
                        break

        cv2.destroyAllWindows()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen

    def get_fullscreen(self):
        return self.fullscreen

    def set_fullscreen(self, set_to: bool):
        self.fullscreen = set_to

    def toggle_pause(self):
        self.pause = not self.pause

    def get_pause(self):
        return self.player.get_pause()

    def set_pause(self, set_to):
        self.player.set_pause(set_to)
    
    def seek(self, pts, relative=False, accurate=False):
        self.player.seek(pts, relative=relative, accurate=accurate)

    def get_volume(self):
        return self.player.get_volume()

    def set_volume(self, volume):
        self.player.set_volume(volume)

    def get_pts(self):
        return int(self.player.get_pts())

    def get_metadata(self):
        return _fix_metadata(self.player.get_metadata())

    def get_frame(self):
        return self.frame

    def get_size(self):
        return self.frame.get_size()

    def set_size(self):
        self.player.set_size()
        

if __name__ == '__main__':
    lePlayer = VideoPlayer(r'C:\code_workspace\stream\StreamIt\test\nice_day.mp4', blocking=False, fullscreen=True)

    print(lePlayer.get_metadata()['duration'])
    while lePlayer.state != 'eof':
        print(lePlayer.get_pts())
        time.sleep(1)
    print(f'eof found!')
