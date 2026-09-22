from setuptools import setup,find_packages

setup(
    name='NetHyTech-STT',
    version='0.1.1',
    author='Sounak Kumar Pradhan',
    author_email='sounakpradhan1980@gmail.com',
    description='this is a speech to text pacakge created by Sounak Kumar Pradhan'
)
packages= find_packages
install_requirements=[
    'selenium',
    'webdriver_manager'
]
