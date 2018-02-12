"""
provisioner-plugin-vmware setup

This is the setup of provisioner-plugin-vmware

:license: MIT, see LICENSE for more details
:copyright: (c) 2018 by Michael Batz, see AUTHORS for more details
"""
import setuptools

setuptools.setup(
    name="provisioner-plugin-vmware",
    version="0.1.0",
    packages=setuptools.find_packages(),

    # meta information
    author="Michael Batz",
    url="https://github.com/michael-batz/opennms-provisioner-plugins",
    license="MIT"

    # requirements
    install_requires=[
        "opennms-provisioner",
        "pyvmomi"
    ],
)
