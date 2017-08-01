from setuptools import setup

setup(
    name='canonicalwebteam.yaml-deleted-paths',
    version='0.1.0',
    author='Canonical Webteam',
    url='https://github.com/ubuntudesign/yaml-deleted-paths',
    packages=[
        'canonicalwebteam.yaml_deleted_paths'
    ],
    description=(
        'Show 410 pages for paths listed in a YAML file.'
    ),
    install_requires=[
        "Django >= 1.3",
        "canonicalwebteam.views-from-yaml >= 0.2.2",
    ],
)

