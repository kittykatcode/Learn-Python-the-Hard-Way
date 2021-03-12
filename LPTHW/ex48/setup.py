try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    config = {
    'description': "my project",
    'author' : ' kritika',
    'url' : 'something.comor',
    'downloadurl': 'something else',
    'author emai': 'hohoho',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'script': [],
    'name': 'projectname'
    }

setup(**config)
