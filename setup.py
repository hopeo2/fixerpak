from setuptools import setup

setup(name='fixer-pak',
      version='0.2',
      description='Fixer service',
      url='https://github.com/omidobeidzadeh/fixerpak',
      author='omid',
      author_email='omidobeidzadeh@gmail.com',
      license='MIT',
      packages=['fixer'],
      install_requires=['requests'],
      zip_safe=False)
