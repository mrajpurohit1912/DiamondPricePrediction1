from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
# def get_requiremnts(file_path:str)->List[str]:
#     requirements = []
#     #req = ""
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements[req.replace("\n","") for req in requirements]
        
#         return requirements

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Mahavir_Rajpurohit',
    author_email="mrajpurohit1912@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)