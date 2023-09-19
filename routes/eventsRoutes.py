from flask import Blueprint

eventsRoutes=Blueprint("eventsRoutess",__name__,url_prefix="/event")

@eventsRoutes.route("/addEvent")
def addEvent():
    return "add event page"