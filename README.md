# cvplayer

cvplayer is a simple wrapper around the ffpyplayer's MediaPlayer class to acheive easy video playback while still having all of the functionality provided by ffpyplayer

### Installation
```
pip install cvplayer
```

there are two ways to use cvplayer, either through
* starting interactive (direct) playback of a video from the command-line: \
```python -m cvplayer filaname``` \
simply starts the video in a different window where it's playback can be controlledby using keymaps \
the default keymaps for controlling the video playback are -

* scripts (getting a VideoPlayer instance and doing whatever you want to)

## scripted access
---
cvplayer provides the VideoPlayer class which is the main wrapper around ffpyplayer's MediaPlayer. \
Initializing a VideoPlayer instance will start playing the video according to the options specified. The Playback can be controlled from within the script as well as using keymaps.

the VideoPlayer class initiates playback and provide methods to control/access the state of the player.

Here's and example to play a video 
```py 
from cvplayer import VideoPlayer

player = VideoPlayer(filename)

while player.state != 'eof':
    print(player.get_pts())
    time.sleep(1)
```


