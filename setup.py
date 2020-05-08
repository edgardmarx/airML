from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='helloworld',
    varsion = '0.0.1', 
    description = 'Saying hello',
    py_modules= ['invoke'],
    package_dir = {'':'src'},

    # classifiers = [

    # ],

    # long_description = long_description,
    # long_description_content_type = "text/markdown"

    
)