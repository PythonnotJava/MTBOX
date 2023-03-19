from setuptools import setup, find_packages

setup(
    name='mtbox',
    version='1.0',
    description='A matplotlib toolbox dedicated to quick start and easy expansion, based on pyqt.',
    author='PythonnotJava',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mtbox=MT:main',
        ],
    },
)
