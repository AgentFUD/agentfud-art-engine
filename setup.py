from setuptools import setup, find_packages

DESCRIPTION = 'Agent FUD Art Engine'
LONG_DESCRIPTION = 'Art Engine which helps you to generate thousands of images - best tool for NFT generation'

def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements


setup(
    name="artengine",
    version="0.1",
    author='Agent FUD',
    author_email='agentfud@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    url='https://github.com/AgentFUD/agentfud-art-engine',
    keywords=['python', 'python3', 'Art Engine', 'NFT Generator', 'NFT', 'Image generator'],
    entry_points="""
        [console_scripts]
        artengine=art_engine.cli:cli
    """,
)
