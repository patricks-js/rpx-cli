from setuptools import find_packages, setup

setup(
    name="rpx",
    packages=find_packages(),
    email='lucas.patrick.lsilva@gmail.com',
    author='Lucas Patrick',
    install_requires=[
        "click",
    ],
    version="0.0.1",
    entry_points="""
    [console_scripts]
    rpx=rpx:rpx
    """
)
