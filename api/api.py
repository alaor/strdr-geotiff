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
    vegetationCover()
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
    print("LONG: {}".format(long))
    print("LAT: {}".format(lat))


def vegetationCover():
    # ref: https://www.hatarilabs.com/ih-en/ndvi-calculation-from-landsat8-images-with-python-3-and-rasterio-tutorial
    # ref: http://www.loicdutrieux.net/pyLandsat/NDVI_calc.html
    RED = dataset.read(3).astype('float64')
    NIR = dataset.read(4).astype('float64')
    # Or can we use np.seterr(divide='ignore', invalid='ignore') and eliminate the need of using astype('float64')
    NDVI = np.where((RED+NIR)==0., 0, (NIR-RED)/(NIR+RED))  # 0.49715062845406466
    print("Vegetation Cover Percentage: {}".format((NDVI.sum() / NDVI.size)))  # 0.4985692579352882

app.run()
