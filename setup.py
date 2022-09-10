from setuptools import find_packages, setup

setup(
    name="rpx",
    packages=find_packages(),
    install_requires=[
        "click",
        "pathlib",
    ],
    version="1.0.0",
    entry_points="""
    [console_scripts]
    rpx=rpx:rpx
    """,
)
