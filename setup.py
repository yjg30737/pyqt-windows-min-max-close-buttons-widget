from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-windows-min-max-close-buttons-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Windows min/max/close buttons widget',
    url='https://github.com/yjg30737/pyqt-windows-min-max-close-buttons-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'python-color-getter>=0.0.1',
        'pyqt-titlebar-buttons-widget @ git+https://git@github.com/yjg30737/pyqt-titlebar-buttons-widget.git@main'
    ]
)