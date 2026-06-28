import numpy as np

def estimate_biomass(ndvi):
    """
    Converts NDVI → biomass estimate
    """

    vegetation = ndvi[ndvi > 0]

    if len(vegetation) == 0:
        return 0.0

    mean_ndvi = np.mean(vegetation)

    # heuristic biomass model (tons/hectare)
    biomass = mean_ndvi * 220

    return float(biomass)