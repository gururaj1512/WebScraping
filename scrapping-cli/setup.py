from setuptools import setup, find_packages

with open('../scrapping/requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().split('\n')

packages = find_packages('../scrapping')
package_dir = {}
for p in packages:
    package_dir[p] = '../scrapping/' + p.replace('.', '/')

setup(
    name='scrapping-cli',
    version='0.0.1',
    install_requires=requirements,
    py_modules=['main'],
    packages=packages,
    package_dir=package_dir,
    entry_points={
        'console_scripts': [
            'scrape = main:default',
            'scrape-import = main:import_scraper',
        ],
    },
)