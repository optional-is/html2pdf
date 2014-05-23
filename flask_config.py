import os

port = int(os.environ.get('PORT', 5000))

# Debug is unsafe, so the default should be debug==False
environment = os.environ.get('HEROKU_ENVIRONMENT', 'LOCAL')

if environment == 'LOCAL':
    print "Running locally with debug=True"
    debug = True
else:
    debug = False
