from setuptools import setup, find_packages


# Used for installing test dependencies directly
tests_require = [
]

setup(
    name='stacutils',
    version='0.0.0',
    description="Space Technologies at Cal's helper code snippets",
    author="Daniel Shen",
    author_email="dshen109@gmail.com",
    packages=find_packages(exclude=['test', 'test_*', 'fixtures']),
    install_requires=[
        "pyserial"
        ],
    test_suite='nose.collector',
    tests_require=tests_require,
    extras_require={'test': tests_require},
    entry_points={
        'console_scripts': [
            ],
        },
)
