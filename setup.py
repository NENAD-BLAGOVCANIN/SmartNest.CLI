from setuptools import setup, find_packages

setup(
    name='smartnest',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        smartnest=main:cli
    ''',
)
