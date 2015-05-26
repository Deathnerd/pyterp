from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
# with codecs_open('README.rst', encoding='utf-8') as f:
#     long_description = f.read()


setup(name='pyfck',
      version='0.0.1',
      description=u"A bare-bones Brainfuck interpreter written in Python 2.7",
      classifiers=[],
      keywords='brainfuck interpreter command-line',
      author=u"Wes Gilleland",
      author_email='wes.gilleland@gmail.com',
      url='https://github.com/Deathnerd/pyfck',
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
      pyfck=pyfck.scripts.cli:cli
      """
      )
