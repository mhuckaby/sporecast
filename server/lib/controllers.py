#!/usr/bin/python2.7
#
#

import os
import webapp2
from webapp2 import Route
from webapp2 import SimpleRoute

#sys.path.append(os.path.join(os.path.dirname(__file__), 'external'))

#from lib.models import FMBUser
from lib.web_request_handler import ErrorNotFoundRequestHandler
from lib.web_request_handler import ErrorInternalRequestHandler

from lib.cors_request_handler import CORSWunderGroundRequestHandler
#from google.appengine.ext import deferred
# Hack to get ndb into the modules list.
#from google.appengine.ext import ndb
#sys.modules['ndb'] = ndb

# last import.
import settings

routes = [
    # Warmup
    Route('/_ah/warmup', handler='lib.www.MushroomObserverHandler'),

    # App
    Route('/app', handler='lib.www.AppHandler'),
    Route('/app/weather/<station>/<year>/<month>',
          handler='lib.www.AppHandler'),
    Route('/app/mob', handler='lib.www.AppHandler'),
    Route('/app/photos', handler='lib.www.AppHandler'),

    Route('/mushroomobserver/<state>/data.json',
          handler='lib.www.MushroomObserverHandler'),
    Route('/', handler='lib.www.AppHandler'),

    # TODO(elsigh): nuke this soon!
    #Route('/<path:(.*)>',
    #      handler='lib.cors_request_handler.CORSStaticRequestHandler'),
    SimpleRoute('/(wunderground/.+)$', CORSWunderGroundRequestHandler),
]

is_debug = True
if 'SERVER_SOFTWARE' in os.environ:
    is_debug = 'Development' in os.environ['SERVER_SOFTWARE']

app = webapp2.WSGIApplication(routes,
                              debug=is_debug)

#app.error_handlers[404] = ErrorNotFoundRequestHandler
#app.error_handlers[500] = ErrorInternalRequestHandler
