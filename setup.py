from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Werkzeug',
    ],
    entry_points={
        'console_scripts': [
            'app = app.app:main',
        ],
    },
)
