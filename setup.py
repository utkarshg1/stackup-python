from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Stack Up Analysis Package'
LONG_DESCRIPTION = 'This package can be used for tolerance stack up analysis for Mechanical Engineers'

with open('requirements.txt','r') as file:
    lines = file.readlines()
    req = [line.strip() for line in lines]

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="stackup-python", 
        version=VERSION,
        author="Utkarsh Gaikwad",
        author_email="gaikwadujg@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=req, # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'        
        keywords=['stack up', 'tolerance', 'mechanical engineering'],
        classifiers= [
            "Development Status :: 1 - Initial Release",
            "Intended Audience :: Mechanical Engineers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)