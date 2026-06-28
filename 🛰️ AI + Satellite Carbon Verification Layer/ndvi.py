import numpy as np

def calculate_ndvi(nir, red):
    nir = nir.astype(float)
    red = red.astype(float)

    ndvi = (nir - red) / (nir + red + 1e-10)
    return np.clip(ndvi, -1, 1)