from setuptools import setup

setup(
    name='dj-rit-auditlog',
    version='0.5.2',
    packages=['auditlog', 'auditlog.migrations', 'auditlog.management', 'auditlog.management.commands'],
    package_dir={'': 'src'},
    url='https://github.com/audiolion/dj-rit-auditlog',
    license='MIT',
    author='Jan-Jelle Kester, Ryan Castner',
    description='Audit log app for Django',
    install_requires=[
        'python-dateutil>=2.6.0,<3.0'
    ],
    zip_safe=False
)
