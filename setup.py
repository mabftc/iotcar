from setuptools import setup

setup(
    name='PiBot',
    packages=['pibot'],
    author = 'Max Bowman',
    author_email = 'maxabowman@gmail.com',
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_socketio'
    ],
    license = 'MIT'
)
