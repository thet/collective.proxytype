# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = "1.0.dev0"
short_description = "Proxy for remote content"
long_description = "\n\n".join([
    open('README.rst').read(),
    open('CHANGES.rst').read()
])


setup(
    name='collective.remoteproxy',
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Johannes Raggam',
    author_email='thetetet@gmail.com',
    url='https://pypi.python.org/pypi/collective.remoteproxy',
    license='GPL version 2',
    packages=find_packages('src'),
    namespace_packages=['collective'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'cssselect',
        'plone.api',
        'plone.app.contentmenu',
        'plone.app.dexterity',
        'requests',
        'lxml',
        # 'beautifulsoup4',
        'setuptools',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
