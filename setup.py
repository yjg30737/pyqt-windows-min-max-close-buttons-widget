from setuptools import setup, find_packages

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
        'python-color-getter @ git+https://git@github.com/yjg30737/python-color-getter.git@main',
        'pyqt-min-max-close-buttons-widget @ git+https://git@github.com/yjg30737/pyqt-min-max-close-buttons-widget.git@main'
    ]
)