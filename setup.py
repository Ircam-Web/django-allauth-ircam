from setuptools import setup, find_packages
from allauth_ircam import __version__
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='django-allauth-ircam',
      version="0.1.0",
      description='Ircam OAuth2 provider for django-allauth',
      long_description=long_description,
      author='Raphaël Voyazopoulos',
      author_email='raphael.voyazopoulos@ircam.fr',
      url='https://github.com/Ircam-Web/django-allauth-ircam',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True)
