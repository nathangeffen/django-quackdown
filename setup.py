from distutils.core import setup

setup(
    name='django-quackdown',
    version='0.5beta',
    description='Web project that tracks untested claims about health-care.',
    author='Nathan Geffen',
    author_email='nathangeffen@gmail.com',
    url='https://launchpad.net/django-quackdown',    
    packages=['quackdown','quackdownproject',],
    license='MIT',
    long_description=open('README').read(),
)
