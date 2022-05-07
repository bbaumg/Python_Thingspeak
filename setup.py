import setuptools 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name='thingspeak',
	version='1.1.1',
	description='Driver for sending Thingspeak data',
	url='https://github.com/bbaumg/Python_Thingspeak',
	author='bbaumg',
	license='MIT',
	packages=['thingspeak'],
	install_requires=['requests']
)
