from importlib.metadata import entry_points
import setuptools 
import pathlib  
from distutils.core import setup 
import pkg_resources 
with pathlib.Path('mathools\\requirements.txt').open() as requirements_txt: 
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]
with pathlib.Path('README.md').open('r') as f: 
    README_txt = f.read()
setup(
    name='mathools', 
    fullname='Math tools', 
    author='Julius Rye Bønnelykke', 
    author_email='juliusrye@gmail.com', 
    version='0.1.1', 
    url = 'https://github.com/JuliusRye/math-extended',
    packages=setuptools.find_packages(),
    # entry_points={
    #     'gui_scripts': [
    #         'feature_disable = vbox_sig_tools.feature_disable:main',
    #     ],
    # },
    description='Some extra math tools', 
    license='MIT License', 
    install_requires=install_requires, 
    long_description=README_txt, 
    long_description_content_type = 'text/markdown',
    setup_requires=["wheel"], 
    include_package_data=True) 