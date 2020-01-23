from connexion.resolver import RestyResolver
import connexion
import os

app = connexion.App(__name__, specification_dir='./')
app.add_api("swagger_api.yml")

@app.route('/')
def home():
    return u"<h1>GeoTIFF's Information API</h1><p>Calculates vegetation cover and some geographical " \
           u"information for a given file in the server (preexisting).</p>" \
           "<p>The information is available on https://alaor-strdr.herokuapp.com/vegetation-cover " \
           "or if you're running local at localhost:5000/vegetation-cover.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
