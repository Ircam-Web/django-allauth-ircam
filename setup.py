from setuptools import setup, find_packages
from organization import __version__
import subprocess

def get_long_desc():
    """Use Pandoc to convert the readme to ReST for the PyPI."""
    try:
        return subprocess.check_output(['pandoc', '-f', 'markdown', '-t', 'rst', 'README.md'])
    except:
        print("WARNING: The long readme wasn't converted properly")

readme = open('README.rst', 'r')
long_desc = readme.read()

setup(name='django-allauth-ircam',
    version=__version__,
    description='Ircam OAuth2 provider for django-allauth',
    long_description=long_desc,
    author='Raphaël Voyazopoulos',
    author_email='raphael.voyazopoulos@ircam.fr',
    url='https://github.com/Ircam-Web/django-allauth-ircam',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
