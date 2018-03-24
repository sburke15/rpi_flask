from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from server import server
from dash_app  import app as app1
from flask_app import app as app2

app = DispatcherMiddleware(server, {'/myflaskapp': app2})

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app)