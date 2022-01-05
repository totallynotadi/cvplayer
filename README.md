# Video Player

cvplayer is a minimal wrapper around the ffpyplayer.MediaPlayer class for playing videos through 
* interactive (direct access to the player through keymaps) or 
* scripts (getting a VideoPlayer instance and doing whatever the user wants to)

audio playback and supplying frames is handles by ffpyplayer and OpenCV is used to display the frames

this makes it useful for simple interactable video playback as well for integrating video playback in programs

## Scripted access
---

cvplayer provides the VideoPlayer class which is the main wrapper around the ffpyplayer. \
Initializing a VideoPlayer instance will start playing the video according to the options specified while initializing. The Playback can be controlled from within the script as well as using keymaps.

### the VideoPlayer class

this class initiates playback and provide methods to control/access the state of the player.

#### &emsp; parameters: _filename_: str
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;the filename of the media to be played

Here's and example to play a video 
```py 
from cvplayer import VideoPlayer

player = VideoPlayer(filename)

duration = int(player.get_metadata()['duration'])
while player.state != 'eof':
    print(player.get_pts())
    time.sleep(1)
```

