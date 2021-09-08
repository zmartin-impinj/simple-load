from setuptools import setup, find_packages
import re

package_name = "simple_load"

setup(
    name=package_name,
    version="0.1dev",
    packages=find_packages(exclude=("tests", "tests.*")),
    url="",
    maintainer="",
    maintainer_email="",
    description="Load testing tool that wraps Locust",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    package_dir={package_name: package_name},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "simple_load = simple_load:main"
        ]
    },
    install_requires=["locustio"]

)
