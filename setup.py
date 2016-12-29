from setuptools import setup

setup(
    name='Ecust',
    version='0.0.3',
    description='Ecust Login Module and Some Functions',
    author='Command',
    author_email='maoxs2@163.com',
    url='http://github.com/maoxs2/Ecust',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='Ecust',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    py_modules=['Ecust', 'jwc_login', 'jwc_functions', 'urp_login', 'urp_functions'],

    scripts=['Ecust_cli.py', 'Ecust.py'],
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
