from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
] 

setup(
    name='REMS',
    version='0.0.1',
    description='Rover Environmental Measurment System',
    long_description=open('README.txt').read(),
    url='',  
    author='James Renick',
    author_email='jrenick@calpoly.edu',
    license='MIT', 
    classifiers=classifiers,
    keywords='rems', 
    packages=find_packages(),
    install_requires=[''] 
)