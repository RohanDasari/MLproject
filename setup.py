from setuptools import find_packages, setup
from typing import List

E_DOT = '-e .'
def get_requirements(file_path : str) -> List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if(E_DOT in requirements):
            requirements.remove(E_DOT)
    return requirements
setup(
    name="MLproject",
    version="0.01",
    author="Rohan Dasari",
    aurthor_email="rohandasari2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)