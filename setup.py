from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '0.1.1'

install_requires = [
    'ipython>=1.0',
]

setup(name='ipython-mongo',
    version=version,
    description="MONGODB access via IPython",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Framework :: IPython',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Programming Language :: Python :: 2',
    ],
    keywords='database ipython mongodb shell',
    author='Yeaji Shin',
    author_email='yeahjishin@gmail.com',
    url='https://github.com/Bloodevil/ipython_mongo',
    download_url='https://github.com/Bloodevil/ipython_mongo/tarball/0.1',
    license='MIT',
    py_modules=['imongo'],
    zip_safe=False,
    install_requires=install_requires,
)
