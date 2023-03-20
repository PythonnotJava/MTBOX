from setuptools import setup, find_packages

setup(
    name='matbox',
    version='1.0.6',
    packages= find_packages(),
    include_package_data=True,
    package_data={
        'matbox': [
            'src/cfg/*.yaml',
            'src/img/*.ico',
            'src/mouseCursor/*.cur',
            'src/QSS/*.qss',
            'src/tutorial/*.md',
            'src/tutorial/*.py'
        ]

    },
    install_requires=[
        'PyQt5',
        'qutepart',
        'pyyaml',
        'qt_material',
        'numpy',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'matbox=MT:main',
        ],
    },

    author='PythonnotJava',
    author_email='',
    description='A matplotlib toolbox dedicated to quick start and easy expansion, based on pyqt.',
    url='https://github.com/PythonnotJava/MTBOX',
    license='MIT',

)
