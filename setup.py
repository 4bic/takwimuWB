import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="takwimuWB",
    version="0.0.1",
    author="Robin Kiplangat",
    author_email="robyne.kiplangat@gmail.com",
    description="The package access and structures World Bank data to Hurumap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/4bic/WB_Data_Wrangling/blob/master/takwimu_wb.ipynb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
