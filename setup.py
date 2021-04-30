from setuptools import setup, find_packages

# call the setup function
setup(
    # name of the project
    name='Robot-Movement',
    # any extras that might me installed
    extras_require=dict(tests=['pytest']),
    # two arguments that let us follow good pytest practices
    # by storing the source code in a directory named differently in our package
    packages=find_packages(where='src'),
    package_dir={"": "src"},
)