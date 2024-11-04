from setuptools import setup, find_namespace_packages


with open('README.md', 'r') as fh:
    readme = '\n' + fh.read()

setup(
    name='pyqtcountrypicker',
    version='1.0.1',
    author='Niklas Henning',
    author_email='business@niklashenning.com',
    license='MIT',
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    package_data={
        'pyqtcountrypicker.flags': ['*.png'],
        'pyqtcountrypicker.hooks': ['*.py']
    },
    install_requires=[
        'QtPy>=2.4.1'
    ],
    python_requires='>=3.7',
    description='A simple, yet highly customizable country picker widget for PyQt and PySide',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/niklashenning/pyqtcountrypicker',
    keywords=['python', 'pyqt', 'pyside', 'qt', 'country-picker'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ]
)
