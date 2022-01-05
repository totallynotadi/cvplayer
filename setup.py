from distutils.core import setup
setup(
    name = 'video_player',
    packages = ['video_player'],
    version = '1.0.0',
    license='MIT',
    description = 'a simple video player written in python using ffpyplayer and OpenCV',
    author = 'addyett',
    author_email = 'g.aditya2048@gmail.com',
    url = 'https://github.com/addyett/video-player',
    download_url = 'https://github.com/addyett/video-player/archive/refs/tags/v1.0.0.tar.gz',
    keywords = ['OpenCV', 'ffpyplayer', 'media-player', 'video'],
    install_requires=[
            'opencv-python',
            'numpy',
            'ffpyplayer',
            'pillow'
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ]
)
