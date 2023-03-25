from setuptools import setup, find_packages

setup(
    name='matbox',
    version='1.0.7',
    packages= find_packages(),
    include_package_data=True,
    package_data={
        'matbox': [
            'Source/cfg/*.yaml',
            'Source/img/*.ico',
            'Source/mouseCursor/*.cur',
            'Source/QSS/*.qss',
            'Source/tutorial/*.mtml',
            'Source/h5/*.html',
            'Source/h5/*.svg',
        ]

    },
    install_requires=[
        'PyQt5',
        'qutepart',
        'pyyaml',
        'qt_material',
        'numpy',
        'matplotlib',
        'PyQtWebEngine'
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
