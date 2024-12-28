from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements ]
        # USing readlines will append \n to it
        # As "-e ." should not be in the file as it is just to trigger setup.py
        # So introduce one condition here
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'MLProject',
    version = '0.0.0.1',
    author = 'Kunal ',
    author_email= 'gauravvaishya143@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    # This will try to get the package name from requirements.txt file
)