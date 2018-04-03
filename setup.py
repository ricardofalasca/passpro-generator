from setuptools import setup, find_packages


setup(
    name='passpro-generator',
    version='1.0.2',
    description="Generate pronounceable passwords",
    url='https://github.com/ricardofalasca/passpro-generator',
    author='Ricardo Falasca',
    author_email='ricardo@falasca.com.br',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
