import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='getuseragent',
    version='0.0.7',
    author="Paul Biswell",
    author_email="pblabsdev@gmail.com",
    description="Get a random, popular, commonly-used user agent string. Random/fake/spoof user agents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pbiswell/getuseragent",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Education',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Education :: Testing',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords=[
        "getuseragent", "get user agent", "random user agent",
        "fake user agent", "fake useragent", "random useragent",
        "spoof useragent", "spoof user agent", "get useragent",
        "useragent", "user agent",
    ],
)
