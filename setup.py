from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()
    f.close()

setup(
    name='pgbackup',
    version='0.0.1',
    author='PM',
    description="A toy project from A Cloud Guru's Introduction to Python Development course"
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pablomuelainco/pgbackup'
    packages=find_packages('src')
)
