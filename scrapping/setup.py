from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().split('\n')

print(find_packages)

setup(
    name='scrapping',
    version='0.0.1',
    install_requires=requirements,
    packages=find_packages()
)