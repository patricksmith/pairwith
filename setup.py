try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Better pair programming git message',
    'author': 'Patrick Smith',
    'url': '',
    'download_url': '',
    'author_email': 'pjs482@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['pairwith'],
    'scripts': [],
    'name': 'pairwith',
    'entry_points': {
        'console_scripts': ['pairwith = pairwith.__main__:main'],
    },
}

setup(**config)
