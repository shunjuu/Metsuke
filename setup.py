from setuptools import setup

setup(
    name='metsuke',
    url='https://github.com/shunjuu/Metsuke',
    author='Kyrielight',
    packages=['metsuke'],
    install_requires=[
        'ayumi @ git+git://github.com/shunjuu/Ayumi@master#egg=ayumi',
        'cerberus'
    ],
    version='0.3',
    license='MIT',
    description='Izumi Message Validator.'
)
