from setuptools import setup, find_packages

setup(
    name='amaranth-cocotb',
    author='Andres Demski',
    packages=find_packages(),
    setup_requires=['cocotb'],
    install_requires=[
        'cocotb-test>=0.2.2',
        'amaranth',
        'amaranth-yosys'
    ]
)
