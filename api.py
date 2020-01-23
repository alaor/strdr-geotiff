import connexion
import os

app = connexion.App(__name__, specification_dir='./')
app.add_api("swagger_api.yml")


@app.route('/')
def home():
    return u"<h1>GeoTIFF's Information API</h1><p>Calculates vegetation cover and some geographical " \
           u"information for a given file in the server (preexisting).</p>" \
           "<p>The information is available <a href='https://alaor-strdr.herokuapp.com/vegetation-cover'>HERE</a> " \
           "or if you're running locally you can also access at <a href='http://localhost:5000/vegetation-cover'>this link</a>.</p>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
