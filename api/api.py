import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return vegetation_cover()

@app.route('/vegetation-cover', methods=['GET'])
def vegetation_cover():
    return "<h1>GeoTIFF's Information API</h1><p>Calculates vegetation cover and some geographical information for a given file in the server (preexisting).</p>"

app.run()