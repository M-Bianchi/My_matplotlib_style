# Code copied from https://stackoverflow.com/questions/31559225/how-to-ship-or-distribute-a-matplotlib-stylesheet

from setuptools import setup
from setuptools.command.install import install
import os
import shutil
import atexit

import matplotlib

def install_mplstyle(stylefile="mystyle.mplstyle"):

    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir() ,"stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)

    print("Installing style into", mpl_stylelib_dir)
    shutil.copy(
        os.path.join(os.path.dirname(__file__), stylefile),
        os.path.join(mpl_stylelib_dir, stylefile))

class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_mplstyle("my_style.mplstyle"))
        atexit.register(install_mplstyle("my_style_NoLaTeX.mplstyle")) 

setup(
    name='my-style',
    version='0.1.0',
    py_modules=['my_style'],
    install_requires=[
        'matplotlib',
    ],
    cmdclass={
        'install': PostInstallMoveFile,
    }
)
