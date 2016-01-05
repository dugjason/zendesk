#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'Zendesk',
	author = 'Victor Duan',
	version = '1.2.0',
	author_email = 'victor.duan@gmail.com',
	packages = ['zendesk'],
	include_package_data = True,
	install_requires = ['requests'],
	license='LICENSE.txt',
	url = 'https://github.com/victorduan/zendesk',
	keywords = 'zendesk api helpdesk',
	description = 'Python API Wrapper for Zendesk',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


