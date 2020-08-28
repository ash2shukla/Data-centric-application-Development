import setuptools

setuptools.setup(
    # CHANGE HERE: with component name
    name="streamlit-component",
    # CHANGE HERE: with the version of your component
    version="0.0.1",
    author="",
    author_email="",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    # CHANGE HERE: the python dependencies
    install_requires=[
        "streamlit >= 0.63",
    ],
)
