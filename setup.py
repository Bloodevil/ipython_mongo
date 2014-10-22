import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
    NEWS = open(os.path.join(here, 'NEWS.txt')).read()
except:
    README = 'https://github.com/Bloodevil/ipython_mongo/blob/master/README.md'
    NEWS = 'https://github.com/Bloodevil/ipython_mongo/blob/master/NEWS.txt'

version = '0.2.0'

install_requires = [
    'ipython>=1.0',
    'pymongo>=2.7',
]

setup(name='ipython-mongo',
    version=version,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
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
    keywords=['database', 'ipython', 'mongodb', 'shell', 'imongo'],
    author='Yeaji Shin',
    author_email='yeahjishin@gmail.com',
    url='https://github.com/Bloodevil/ipython_mongo',
    download_url='https://github.com/Bloodevil/ipython_mongo/tarball/0.2',
    license='MIT',
    py_modules=['imongo'],
    zip_safe=False,
    install_requires=install_requires,
)
