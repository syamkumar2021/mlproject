from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # whenever it read line by line it will add "\n" for each line we read
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
setup(
    name="mlproject",
    version="0.0.1",
    author="Syam Kumar",
    author_email="syamkumar.chimakumar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # whatever libraries i want I write it over here,and automatically install the libraries
                                                   # there will be many packages,can not write like this: install_requires=["pandas","numpy","seaborn"],so we carate a function and indide we give 'requirements.txt'
    
)