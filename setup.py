from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().split('\n')

setup(
    name='my_package',
    version='0.0.1',
    install_requires=requirements,
    packages=find_packages(include=['basics', 'scrapping', 'scrapping.*']),
    entry_points={
        'console_scripts': [
            'scrape = scrapping.main:default',
        ],
    },
)