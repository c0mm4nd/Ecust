from setuptools import setup,find_packages

setup(
    name='Ecust',
    version='0.0.2',    
    description='Ecust Login Module and Some Functions',
    author='Command',
    author_email='maoxs2@163.com',    
    url='http://github.com/maoxs2/Ecust',    
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    scripts=['Ecust_cli.py','Ecust.py'],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'Ecust_cli = Ecust_cli:main',
        ],
    },
    install_requires=[
        "lxml",
        "requests",
    ],
)
