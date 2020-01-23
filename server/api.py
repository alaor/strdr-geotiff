from connexion.resolver import RestyResolver
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api("swagger_api.yml")

@app.route('/')
def home():
    return u"<h1>GeoTIFF's Information API</h1><p>Calculates vegetation cover and some geographical " \
           u"information for a given file in the server (preexisting).</p>" \
           "<p>The information is available on localhost:5000/vegetation-cover.</p>"


app.run(debug=True)
