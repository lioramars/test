from flask import Flask,Blueprint
from routes.indexRoutes import indexRoutes
from routes.eventsRoutes import eventsRoutes
app=Flask(__name__)
app.register_blueprint(indexRoutes)
app.register_blueprint(eventsRoutes)