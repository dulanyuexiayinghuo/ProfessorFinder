from setuptools import setup
import codecs
import ProfessorFinder


def read(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        return f.read()


long_description = read('README.rst')  # use pandoc to automatically generate README.rst from README.md

setup(
    name='ProfessorFinder',
    version=ProfessorFinder.__version__,
    licence='',
    url='',
    author='',
    author_email='',
    install_requires=[],  # python freeze > requirements.txt
    description='',
    long_description=long_description,
    packages=['ProfessorFinder'],
    platforms='',
    classifiers=[],
    extras_require={}
)
