from setuptools import setup, find_packages

VERSION = '0.0.0'
PACKAGE_NAME = 'useless_pkg'
AUTHOR = 'None'
AUTHOR_EMAIL = 'noone@email.com'
URL = 'https://github.com/madenindya/useless_pkg'
REQUIRES_PYTHON = '>=3.8.0'
LICENSE = 'MIT License'
DESCRIPTION = 'Nothing important'
LONG_DESCRIPTION = "haha hihi"
LONG_DESC_TYPE = "text/markdown"


def parse_requirements():
    with open("requirements.txt", "r") as fh:
        reqs_a = fh.read()
        reqs_a = reqs_a.split('\n')
    return reqs_a


reqs = parse_requirements()


setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      python_requires=REQUIRES_PYTHON,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=reqs,
      packages=find_packages(exclude=['tests'])
      )
