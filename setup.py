from setuptools import setup, find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements mentioned in the requirements.txt file
    '''
    with open(file_path, 'r') as file:
        #requirements = file.readlines()
        #requirements = [req.replace('\n',"") for req in requirements]
        requirements = file.read().splitlines()     #.splitlines() will split the file into lines and return a list of lines
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)    # Remove the '-e .' from the requirements list if it is present
    return requirements



setup(
    name = 'cortexflow',
    version = '0.1.0',
    author='Bikram',
    author_email='bikrambanerjee32@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
