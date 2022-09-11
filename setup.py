from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name="rpx_cli",
    packages=["rpx"],
    # packages=find_packages(),
    autor_email="lucas.patrick.lsilva@gmail.com",
    author="Lucas Patrick",
    description="CLI for react projects",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT License",
    install_requires=["click", "pathlib"],
    version="0.0.9",
    entry_points="""
    [console_scripts]
    rpx=rpx:rpx
    """
)
