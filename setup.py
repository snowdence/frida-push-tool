from setuptools import setup

from frida_push_tool import __version__

setup(
    name='frida-push-tool',
    version=__version__,
    packages=['frida_push_tool'],
    url='https://github.com/snowdence/frida-push-tool',
    license='GPLv3',
    author='AndroidTamer',
    author_email='github@androidtamer.com',
    description='Wrapper tool to identify the remote device and push device specific frida-server binary.',
    install_requires=['requests', 'frida', 'future'],
    entry_points={
        'console_scripts': [
            'frida-push-tool = frida_push_tool.command:main'
        ]
    }
)
