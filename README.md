=====================
Python RightScale API
=====================

This project aims to give you a more sane interface to RightScale than would
hacking at the REST api yourself.

Current State
-------------

This project is a work in progress. Functionality is limited, but this will give you
the ability to perform some basic operations.

Installing
----------

Releases of this can be found on Python PI: http://pypi.python.org/pypi/rightscale/
Installation can be performed with pip: `pip install rightscale`

Contributing
------------

You are welcome to fork, and file bugs on github (http://github.com/kshenk1/python-rightscale)

Examples
--------

::
	from rightscale import RightScale
	rsapi = RightScale(account_number, username, password)

	# Find 'me' in RightScale.
	myself = rsapi.whoami()

	# What does RightScale call me? (The server name in the UI)
	print myself.nickname

	# Change my server name in RightScale
	myself.nickname = "New server name"
	myself.save()

	# What tags do I have?
	print myself.tags

	# How many servers do we have?
	print len(rsapi.servers)

Author
------

This library was originally written by Jordan Sissel and has contributions from several other developers.
You can view the original here: https://github.com/jordansissel/python-rightscale
