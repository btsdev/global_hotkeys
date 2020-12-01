from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='global_hotkeys',
  version='0.0.3',
  description='',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/btsdev',
  author='btsdev',
  author_email='btsdevman@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='hotkeys,shortcuts',
  packages=find_packages(),
  install_requires=[], # "some_lib ~= 1.0"
  extras_require = {
    "dev": [] # "pytest>=3.7"
  }
)