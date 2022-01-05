import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="cvplayer",
    version="1.0.0",
    description="a simple video player written in python using ffpyplayer and OpenCV",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/addyett/video-player",
    author="addyett",
    author_email="g.aditya2048@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5+",
    ],
    packages=["cvplayer"],
    include_package_data=True,
    install_requires=["opencv-python", "ffpyplayer", 'numpy', 'pillow'],
    entry_points={
        "console_scripts": [
            "videoplayer=video_player.__main__:main",
        ]
    },
)
