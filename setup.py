import sys
import os
import setuptools
from pathlib import Path


with open("README.md", "r") as fh:
    long_description = fh.read()
    
modules = [os.path.join('modules', item) for item in os.listdir('snippets/modules')]
print(modules)

setuptools.setup(
    name='snippets',
    version='0.1.0',
    author="streanger",
    description="python snippets viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/streanger/snippets",
    packages=['snippets',],
    install_requires=['pyperclip', 'rich'],
    include_package_data=True,
    package_data={
        'modules': modules,
    },
    entry_points={
        "console_scripts": [
            "snippets=snippets:viewer",
        ]
    },
)
