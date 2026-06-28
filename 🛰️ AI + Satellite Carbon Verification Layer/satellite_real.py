import numpy as np

def fetch_satellite_tile(bbox, time_step):
    """
    REAL SYSTEM PLACEHOLDER:
    Replace with Sentinel-2 / Google Earth Engine API call

    Returns simulated multispectral tile
    """

    np.random.seed(time_step)

    # simulate multispectral bands
    tile = np.random.rand(4, 512, 512)

    return {
        "red": tile[0],
        "green": tile[1],
        "blue": tile[2],
        "nir": tile[3]
    }