# coding: utf-8

import logging
import flask
import flask_config
import phantom

app = flask.Flask(__name__)
app.static_folder = "public"
app.SEND_FILE_MAX_AGE_DEFAULT = 0
	
@app.route('/')
def pdf():
	
	
	"""Returns html that is useful for understanding, debugging and extending
	the charting API"""

	return file('public/pdf.html').read()
			
@app.route('/html-to-pdf', methods=['POST'])
def html_to_pdf():
	
	"""Takes an HTTP POST with html, renders a pdf using phantomjs and returns
	a pdf.

	Example use with jQuery:

		$.post('/html-to-pdf', {'html': HTML})

	"""
	html = flask.request.form.get('html', '')
	title = 'html2pdf'

	try:
		pdf_data = phantom.html_to_pdf(html)
	except OSError as e:
		# Reraise the error so flask can log it
		raise e

	if pdf_data:
		response = flask.make_response(pdf_data)
		response.headers['Cache-Control'] = 'no-cache'
		response.headers['Content-Type'] = 'application/pdf'
		response.headers['Content-Disposition'] = "attachment;filename=%s.pdf"%title
		return response

	else:
		flask.abort(400)


if __name__ == '__main__':
	# Set up logging to stdout, which ends up in Heroku logs
	stream_handler = logging.StreamHandler()
	stream_handler.setLevel(logging.WARNING)
	app.logger.addHandler(stream_handler)

	app.debug = True
	app.run(host='0.0.0.0', port=flask_config.port)
