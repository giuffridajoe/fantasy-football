try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Joe Giuffrida',
        'url': 'URL where this project can be found.',
        'download_url': 'Where to download this porject.',
        'author_email': 'giuffridajoe@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['main-module-name'],
        'scripts': [],
        'name': 'projectname'}

setup(**config)
