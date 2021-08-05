import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bg_mpl_stylesheet",  # Replace with your own name
    version='0.1.0',
    author="Simon J. L. Billinge",
    author_email="sb2896@columbia.edu",
    description="A package for using Billinge group style files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Billingegroup/mpl-stylesheets",
    packages=setuptools.find_packages(),
    package_dir={"bg_mpl_stylesheet": "bg_mpl_stylesheet"},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    data_files=[("", ["LICENSE.txt"])],
    python_requires='>=3.6',
    zip_safe=False,
)
