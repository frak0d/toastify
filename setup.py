import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
	name="toastify",
	version="1.1.5",
	description="Simple and Lighweight Windows 10 Toast Notifications.",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/Tanishq-Banyal",
	author="Tanishq-Banyal",
	author_email="banyaltanishq@gmail.com",
	license="MIT",
	classifiers=[
		"Environment :: Win32 (MS Windows)",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Development Status :: 5 - Production/Stable",
		"Operating System :: Microsoft :: Windows :: Windows 10",
	],
	packages=["toastify"],
	include_package_data=True,
	#install_requires=[],
)