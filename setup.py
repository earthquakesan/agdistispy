from distutils.core import setup

setup(
    name='agdistispy',
    version='1.0.5',
    author='Ivan Ermilov',
    author_email='earthquakesan@gmail.com',
    packages=['agdistispy'],
    scripts=[],
    url='http://pypi.python.org/pypi/agdistispy/',
    license='LICENSE.txt',
    description='Python bindings for AGDISTIS - Multilingual Disambiguation of Named Entities Using Linked Data.',
    long_description=open('README.txt').read(),
    install_requires=[
        'requests'
    ],
)

