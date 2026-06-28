import numpy as np
from ndvi import calculate_ndvi
from biomass import estimate_biomass


def build_training_sample(tile1, tile2):
    """
    Convert satellite time-series into ML dataset sample
    """

    ndvi1 = calculate_ndvi(tile1["nir"], tile1["red"])
    ndvi2 = calculate_ndvi(tile2["nir"], tile2["red"])

    biomass1 = estimate_biomass(ndvi1)
    biomass2 = estimate_biomass(ndvi2)

    return {
        "features": {
            "mean_ndvi_t1": float(np.mean(ndvi1)),
            "mean_ndvi_t2": float(np.mean(ndvi2)),
            "delta_ndvi": float(np.mean(ndvi2 - ndvi1))
        },
        "label": {
            "biomass_change": biomass2 - biomass1
        }
    }