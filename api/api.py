import flask
import rasterio
import numpy as np
from affine import Affine
from pyproj import Proj, transform

app = flask.Flask(__name__)
app.config["DEBUG"] = True

path = "../sources/analytic.tif"
dataset = rasterio.open(path)


@app.route('/', methods=['GET'])
def home():
    centroid()
    return vegetation_cover()


@app.route('/vegetation-cover', methods=['GET'])
def vegetation_cover():
    return "<h1>GeoTIFF's Information API</h1><p>Calculates vegetation cover and some geographical information for a given file in the server (preexisting).</p>"


def centroid():
    # ref: https://github.com/EarthScientist/etc/blob/master/centroid_from_raster.py
    # T0 = r.affine  # not working, fix below, solution found at: https://github.com/mdbartos/pysheds/issues/13
    T0 = dataset.transform  # upper-left pixel corner affine transform
    p1 = Proj(dataset.crs)
    A = dataset.read(1)  # pixel values

    # All rows and columns
    cols, rows = np.meshgrid(np.arange(A.shape[1]), np.arange(A.shape[0]))
    # Get affine transform for pixel centres
    T1 = T0 * Affine.translation(0.5, 0.5)
    # Function to convert pixel row/column index (from 0) to easting/northing at centre
    rc2en = lambda r, c: (c, r) * T1
    # All eastings and northings -- this is much faster than np.apply_along_axis
    eastings, northings = np.vectorize(rc2en, otypes=[np.float, np.float])(rows, cols)
    # Project all longitudes, latitudes as EPSG:4326
    longs, lats = transform(p1, p1.to_latlong(), eastings, northings)
    long = longs.sum() / longs.size
    lat = lats.sum() / lats.size
    print("LONG: {}".format((longs.sum() / longs.size)))
    print("LATS: {}".format((lats.sum() / lats.size)))


app.run()
