# Test for Python version 2 only
import sys
if not sys.version_info[0] == 2:
    print "Sorry, but Python 3 isn't inherently supported yet"
    sys.exit(1)

from setuptools import setup, find_packages

setup(name='pyterp',
      version='0.1',
      description=u"A bare-bones collection of interpreters written in Python 2.7. Currently only supports Brainfuck. It's guaranteed to have bugs",
      classifiers=[],
      keywords='brainfuck interpreter command-line',
      author=u"Wes Gilleland",
      author_email='wes.gilleland@gmail.com',
      url='https://github.com/Deathnerd/pyterp',
      download_url='https://github.com/Deathnerd/pyterp@master',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      pyterp=pyterp.scripts.cli:cli
      """
      )
