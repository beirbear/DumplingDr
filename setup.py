from setuptools import setup

setup(name='data_repository',
      version='0.1.0',
      packages=['data_repository'],
      entry_points={
          'console_scripts': [
              'data_repository = data_repository.__main__:main'
          ]
      }
      )
