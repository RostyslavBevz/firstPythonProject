from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Convert Celcius',
    version='0.0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['celsius2fahren = convercelcius.Convert.py:ask_user']
    }
)
