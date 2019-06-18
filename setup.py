from setuptools import setup

setup(
    name = 'bt-config',
    version = '0.1.0',
    packages = ['btconfig'],
    entry_points = {
        'console_scripts': [
            'bt-config = btconfig.__main__:main'
        ]
    })