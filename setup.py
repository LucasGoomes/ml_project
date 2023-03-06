from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT= '-e .'
def get_requirements(file_path:str)-> List:
    """Essa função retorna a lista de requirements"""
    requirements=[]
    with open(file_path) as arq:
        requirements = arq.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements 

setup(
name='mlproject',
version='0.0.1',
author='Lucas Gomes',
author_email='luucas.gomeswk@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)