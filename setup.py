from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
  requirements=[]
  with open('requirement.txt') as file_bj:
    requirements=file_bj.readlines()
    requirements=[req.replace("\n","") for req in requirements]

    if  HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
  return requirements
setup(
    name="mlproject",
    version='0.1',
    author='raheleh',
    packages=find_packages(),
    install_requiers=get_requirements('requirement.txt')


)