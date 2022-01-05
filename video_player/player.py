import threading
import time

import cv2
import numpy
from ffpyplayer.player import MediaPlayer
from PIL import Image


class VideoPlayer ():
    def __new__(self, term, paused=False) -> MediaPlayer:
        opts = {'sync': 'audio', 'autoexit': True, 'paused': paused}
        self.player = MediaPlayer(term, ff_opts=opts)
        time.sleep(30)
        self.pause = self.player.get_pause()
        self.fullscreen = False
        handler_thread = threading.Thread(target=self.player_handler, args=(self, ))
        handler_thread.start()
        return self

    def player_handler(self):
        if not self.pause:
            self.player.toggle_pause()
        while True:
            frame, val = self.player.get_frame()
            if val != 'eof':
                if int(self.player.get_pts()) == int(self.player.get_metadata()['duration']):
                    time.sleep(0.5)
                    self.player.toggle_pause()
                    self.player.close_player()
                    break
                if isinstance(val, str):
                    waitkey = 32
                elif int(val) == 0:
                    waitkey = 32
                else:
                    waitkey = int(val * 100)
                pressed_key = cv2.waitKey(waitkey) & 0xFF
                if pressed_key != 255:
                    if pressed_key == ord('q') or pressed_key == 81 or pressed_key == 27:
                        break
                    elif pressed_key == ord(' ') or pressed_key == ord('k') or pressed_key == 75:
                        if self.pause is False:
                            self.pause = True
                        elif self.pause is True:
                            self.pause = False
                        self.player.toggle_pause()
                        print('toggled pause')
                    elif pressed_key == ord('l') or pressed_key == 76:
                        print('skiping ahead')
                        self.player.toggle_pause()
                        self.player.seek(5, relative=True, accurate=False)
                        self.player.toggle_pause()
                        self.player.get_frame()
                    elif pressed_key == ord('j') or pressed_key == 74:
                        print('heading behind')
                        self.player.toggle_pause()
                        self.player.seek(-5, relative=True, accurate=False)
                        self.player.toggle_pause()
                        self.player.get_frame()
                    elif pressed_key == ord('f'):
                        print('toggled fullscreen mode')
                        if self.fullscreen is False:
                            self.fullscreen = True
                        elif self.fullscreen is True:
                            self.fullscreen = False

                if not self.pause:
                    if frame is not None:
                        image, pts = frame
                        x, y = image.get_size()
                    else:
                        x, y = '', ''

                    if val != 'eof' or frame is not None:
                        cv2.namedWindow('video', cv2.WINDOW_KEEPRATIO)
                        if self.fullscreen is True:
                            cv2.setWindowProperty(
                                'video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                        elif self.fullscreen is False:
                            if x != '' and y != '':
                                cv2.resizeWindow('video', x, y)
                            cv2.setWindowProperty(
                                'video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
                        if frame is not None:
                            image, pts = frame
                            x, y = image.get_size()
                            data = image.to_bytearray()[0]
                            image =  Image.frombytes("RGB", (x, y), bytes(data))
                            image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
                            cv2.imshow('video', image)
                    else:
                        break
                else:
                    cv2.imshow('video', numpy.zeros((512, 512, 3), dtype = "uint8"))
                    pressed_key = cv2.waitKey(0) & 0xFF
                    if pressed_key != 255:  print(pressed_key)
                    if pressed_key == ord(' ') or pressed_key == ord('k') or pressed_key == 75:
                        print(f'pressed key is {pressed_key}')
                        self.pause = False
                        self.player.toggle_pause()

        print('exiting')
        cv2.destroyAllWindows()

    def toggle_fullscreen(self):
        if self.fullscreen is True:
            self.fullscreen = False
        if self.fullscreen is False:
            self.fullscreen = True
