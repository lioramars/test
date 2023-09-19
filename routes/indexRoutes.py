from flask import Blueprint

indexRoutes=Blueprint("users",__name__,url_prefix="/test")

@indexRoutes.route("/")
def index():
    return "<h1>hello world</h1>"
