from setuptools import setup, find_packages

setup(
    name='SimpleProfiler',
    version='0.1.0',
    description='A simple package that can be added to a project to diagnose slower areas of the code that need optimisation.'
                'This project was built out of necessity as many other examples are either to complex or cumbersome, or they'
                'treat all code as stationary, that it doesnt get slower overtime as input change. This is obviously untrue.'
                'Therefore this project is able to diagnose slow areas of the code and also see how execution time changes over time.',
    author='Matthew Hewitt',
    author_email='',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'tqdm'
    ],
)
