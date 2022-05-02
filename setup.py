import setuptools 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name='Python_Thingspeak',
	version='1.1',
	description='Driver for sending Thingspeak data',
	url='https://github.com/bbaumg/Python_Thingspeak',
	author='bbaumg',
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
  ],
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src"),
	install_requires=['requests'],
	zip_safe=False)
