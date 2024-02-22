import os
import sys
from pathlib import Path

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

modules = [os.path.join('modules', item) for item in os.listdir('snippets/modules')]
print(modules)
version_path = Path(__file__).parent / 'snippets/__version__.py'
version_info = {}
exec(version_path.read_text(), version_info)

setuptools.setup(
    name='snippets',
    version=version_info['__version__'],
    author="streanger",
    description="python snippets viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/streanger/snippets",
    packages=['snippets',],
    install_requires=['pyperclip', 'rich', 'setuptools', 'black'],
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
