from setuptools import setup

setup(
    name='metsuke',
    url='https://github.com/shunjuu/Metsuke',
    author='Kyrielight',
    packages=['metsuke'],
    install_requires=[
        'ayumi @ git+https://github.com/shunjuu/Ayumi',
        'cerberus'
    ],
    version='0.3',
    license='MIT',
    description='Izumi Message Validator.'
)
