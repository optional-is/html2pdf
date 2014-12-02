# coding: utf-8

import tempfile
import subprocess
import md5
import datetime


def html_to_pdf(html):
	"""Runs phantomjs in a subprocess to render html into a pdf 

	Args:
		html: String of html to render

	Returns:
		The pdf data in a string. If phantomjs doesn't like the html,
		this string can end up empty.

	Raises:
		OSError: An error occured in running the phantomjs subprocess

	"""

	# TODO: Use stdin and stdout instead of tempfiles, as Heroku makes no
	# guarantees about tempfiles not being destroyed mid-request. This may
	# require use of phantomjs version 1.9, which (as of 2013-3-2) hasn't been
	# released
	html_tmp = tempfile.NamedTemporaryFile(mode='w+b', dir="phantom-scripts", suffix='.html')
	pdf_tmp	 = tempfile.NamedTemporaryFile(mode='r+b', suffix='.pdf')
		
	# edit rasterize_pdf to change size/header+footer settings
	# maybe expose some options here if we need them
	phantom_cmd = [ 'phantomjs',
					'phantom-scripts/rasterize_pdf.js',
					'--output-encoding=utf8',
					'%s' % html_tmp.name,
					'%s' % pdf_tmp.name]

	try:
		html_tmp.write(html.encode('utf8'))
		html_tmp.flush()

		print subprocess.call(phantom_cmd)

		return pdf_tmp.read()

	finally:
		html_tmp.close()
		pdf_tmp.close()