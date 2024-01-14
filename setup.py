from setuptools import setup, find_packages

setup(
    name='ipshita-flaskapp',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Werkzeug',
    ],
    entry_points={
        'console_scripts': [
            'ipshita-flaskapp = ipshita-flaskapp.app:main',
        ],
    },
)
