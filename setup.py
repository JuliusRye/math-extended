from importlib.metadata import entry_points
import setuptools 
import pathlib  
from distutils.core import setup 
import pkg_resources 
with pathlib.Path('mathext\\requirements.txt').open() as requirements_txt: 
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]
setup(
    name='math_extended', 
    fullname='', 
    author='Julius Rye Bønnelykke', 
    author_email='juliusrye@gmail.com', 
    version='0.1', 
    packages=setuptools.find_packages(),
    # entry_points={
    #     'gui_scripts': [
    #         'feature_disable = vbox_sig_tools.feature_disable:main',
    #     ],
    # },
    description='Some extra fun math tools', 
    license='MIT License', 
    install_requires=install_requires, 
    long_description="", 
    setup_requires=["wheel"], 
    include_package_data=True) 