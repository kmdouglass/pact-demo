from setuptools import find_packages, setup

with open('requirements.txt') as fh:
    requirements = fh.read().splitlines()

config = {
    'description': 'Pact demo',
    'install_requires': requirements,
    'name': 'pact_demo',
    'packages': find_packages(),
}

setup(**config)
