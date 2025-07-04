# Code copied from https://stackoverflow.com/questions/31559225/how-to-ship-or-distribute-a-matplotlib-stylesheet

from setuptools import setup
from setuptools.command.install import install
import os
import shutil
import atexit

import matplotlib

def install_mplstyle():
    style_files = ["mystyle.mplstyle", "mystyle_NoLaTeX.mplstyle"]

    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)

    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in style_files:
        src = os.path.join(os.path.dirname(__file__), stylefile)
        dst = os.path.join(mpl_stylelib_dir, stylefile)
        shutil.copy(src, dst)

class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_mplstyle)

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

