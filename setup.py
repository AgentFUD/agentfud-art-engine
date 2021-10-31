from setuptools import setup, find_packages
from pathlib import Path
import os, pathlib

DESCRIPTION = 'Agent FUD Art Engine'

this_directory = pathlib.Path(__file__).parent.resolve()
with open(os.path.join(this_directory, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements


setup(
    name="agentfud-art-engine",
    version="0.2.3",
    author='Agent FUD',
    author_email='agentfud@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    url='https://github.com/AgentFUD/agentfud-art-engine',
    keywords=['python', 'python3', 'Art Engine', 'NFT Generator', 'NFT', 'Image generator'],
    entry_points="""
        [console_scripts]
        artengine=art_engine.cli:cli
    """,
    classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
   ],
   python_requires='>=3.6'
)
