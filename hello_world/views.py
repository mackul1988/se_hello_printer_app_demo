from hello_world import app
from hello_world.formater import get_formatted, SUPPORTED, PLAIN
from flask import request


my_name = "Maciej"
msg = "Hello World!"

@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, my_name, output.lower())


@app.route('/outputs')
def supported_outpu():
    return ", ".join(SUPPORTED)