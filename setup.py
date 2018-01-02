from distutils.core import setup

setup(
    name='dj-rit-auditlog',
    version='0.4.4',
    packages=['auditlog', 'auditlog.migrations', 'auditlog.management', 'auditlog.management.commands'],
    package_dir={'': 'src'},
    url='https://github.com/audiolion/dj-rit-auditlog',
    license='MIT',
    author='Jan-Jelle Kester, Ryan Castner',
    description='Audit log app for Django',
    install_requires=[
        'django-jsonfield>=1.0.0',
        'python-dateutil==2.6.0'
    ],
    zip_safe=False
)