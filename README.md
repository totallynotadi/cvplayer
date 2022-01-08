# cvplayer

cvplayer is a video player written in python that provides easy video playback using ffpyplayer and OpenCV 

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

parameters for a VideoPlayer instance:

| parameter    | type  |Description                                                                                                                   |
|--------------|-------|------------------------------------------------------------------------------------------------------------------------------|
| filename     | str   | The filename of the media                                                                                                    |
| paused       | bool  | If True, the player will be in a paused state after creation, otherwise it will immediately start playing. Defaults to False |
| fullscreen   | bool  | If True, the video playback will be in fullscreen mode immediately after it's creation. Defaults to True                     |
| key_controls | bool  | If True, the video playback can be controlled using specified keymaps. Defaults to True                                      | 
| skip_interval| int   | Specify the numebr of seconds to move ahead or beind when navigating the video using the keymaps                             |
| volume       | float | The default volume. A value between 0.0 - 1.0. Defaults to 1.0                                                               |
| mute         | bool  | If True, the player will be muted by default after creation. Defaults to False                                               |
| t            | int   | Play only ```t``` seconds of the audio/video. Defaults to the full audio/video. Defaults to the full audio/video             |
| ss           | int   | Seek to pos ```ss``` into the file when starting. Defaults to the beginning of the file                                      |
| blocking     | bool  | If True, the playback will block the current thread (the one it's being run from) until the playback ends. Defaults to False |
| playback     | bool  | If False, only the player will be initialized and no video/audio will be played, only audio can be played by unmuting the player. Useful for just reading the frames form a video to display them using something else|
