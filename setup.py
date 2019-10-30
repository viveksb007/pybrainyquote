from setuptools import setup

setup(
    name='brainyquote',
    packages=['brainyquote'],
    version='0.2',
    description='Fetches and Returns quotes from www.brainyquote.com',
    author='Vivek Singh Bhadauria',
    author_email='viveksbhadauria007@gmail.com',
    url='https://github.com/viveksb007/pybrainyquote',
    download_url ='https://github.com/viveksb007/pybrainyquote/tarball/0.2',
    keywords = ['quotes', 'pyquotes', 'brainyquote'],
    classifiers = [],
    install_requires=[
        "beautifulsoup4",
		"requests"
    ]
    )
