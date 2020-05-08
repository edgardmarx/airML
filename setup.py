from setuptools import setup

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name='airML',
    varsion = '0.0.1', 
    description = 'application will allow users (including us)'+
                  'to share and dereference ML models.',
    py_modules= ['airML'],
    package_dir = {'':'src'},

    # classifiers = [
    # ],

    # long_description = long_description,
    # long_description_content_type = "text/markdown"
)