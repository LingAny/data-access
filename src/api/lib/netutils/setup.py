import os
from setuptools import setup
from setuptools import find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='netutils',
    version='18.2.1',
    author='Russian Telecommunication Equipment Company',
    author_email='info@pkcc.ru',
    description='Network tools',
    license='1. Restricted Uses /n/t1.1. No Distribution, etc. [Licensee] [You] may not distribute, license, loan, '
            'or sell the Software or other content that is contained or displayed in it./n/t1.2. No Modification. '
            '[Licensee] [You] may not modify, alter, or create any derivative works of the Software./n/t'
            '1.3. No Reverse Engineering. [Licensee] [You] may not reverse engineer, decompile, decode, decrypt, '
            'disassemble, or derive any source code from the Software./n/t1.4. Proprietary Notices. '
            '[Licensee] [You] may not remove, alter, or obscure any copyright, trademark, or other proprietary rights '
            'notice on or in the Software.',
    keywords='Network tools',
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities"
    ], install_requires=[
        "asynqp",
        "python-dateutil",
        "pyserial-asyncio",
        "pyserial",
        "nameko"
    ]
)
