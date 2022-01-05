# Video Player

a minimal video player written in python using ffpyplayer and OpenCV.

Video Player provides interactive as well as scripted access to the video playback, either through keyboard keys or through scripting

this makes it useful for simple interactable video playback that can be controlled by users as we all for developers to get a instance of the VideoPlayer and do whatever they want with it while decding if the end user can interact with the playback.

### Scripted access
---
```py 
from cvplayer import VideoPlayer

player = VideoPlayer(filename)

while True:
    current_pts = player.get_pts()
    print(current_pts)
    time.sleep(1)
```
