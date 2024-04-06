'''
# find all packages automatically in entire ml folder that we created
from setuptools import find_packages,setup
from typing import List

# while reading requirments.txt file, ignore -e . 
HYPEN_E_DOT='-e .'              

def get_requirements(file_path:str)->List[str]:
    '''
'''
    this will return list of requirments
'''
    
'''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()

        ## replace \n with space in requirements.txt file 
        requirments=[req.replace("\n"," ") for req in requirments]

        # while reading requirments.txt file, ignore -e . 
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    
    return requirments 


# metadata of project
setup(
name='mlproject',
version='0.0.1',
author='Aniket',
author_email='aniketdandekar220@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirments.txt')
)
'''

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Aniket',
author_email='aniketdandekar220@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)