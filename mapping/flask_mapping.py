import flask
import logging
# Our own modules
import pre  # Pre-process schedule file
import config  # Configure from configuration files or command line

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
app.map_key = CONFIG.MAP_KEY
POI = pre.process(open(CONFIG.POI))
logging.info(POI)


###
# Pages
# Each of these transmits the default "200/OK" header
# followed by html from the template.
###

@app.route("/")
@app.route("/index")
def index():
    """Main application page; most users see only this"""
    app.logger.debug("Main page entry")
    flask.g.POI = POI  # To be accessible in Jinja2 on page
    return flask.render_template('mapping.html')


@app.route("/refresh")
def refresh():
    """Admin user (or debugger) can use this to reload the schedule."""
    app.logger.debug("Refreshing schedule")
    global POI
    POI = pre.process(open(CONFIG.POI))
    return flask.redirect(flask.url_for("index"))


### Error pages ###
#   Each of these transmits an error code in the transmission
#   header along with the appropriate page html in the
#   transmission body


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.g.linkback = flask.url_for("index")
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def i_am_busted(error):
    app.logger.debug("500: Server error")
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def no_you_cant(error):
    app.logger.debug("403: Forbidden")
    return flask.render_template('403.html'), 403


#
# If run as main program (not under gunicorn), we
# turn on debugging.  Connects to anything (0.0.0.0)
# so that we can test remote connections.
#

#############


app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
