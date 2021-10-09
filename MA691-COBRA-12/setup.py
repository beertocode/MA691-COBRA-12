import setuptools
#replace toolbox with package folder name later
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='MA691-COBRA-12',
    version='0.0.3',
    
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/beertocode/MA691-COBRA-12',
    project_urls = {
        "Bug Tracker": "https://github.com/beertocode/MA691-COBRA-12/issues"
    },
    packages=['MA691-COBRA-12'],
    install_requires=['requests'],
)
