from satellite import get_satellite_image
from ndvi import calculate_ndvi
from biomass import estimate_biomass


def analyze_time_series(t1: int, t2: int):
    """
    Compare two time steps of satellite data
    """

    red1, nir1 = get_satellite_image(t1)
    red2, nir2 = get_satellite_image(t2)

    ndvi1 = calculate_ndvi(nir1, red1)
    ndvi2 = calculate_ndvi(nir2, red2)

    biomass1 = estimate_biomass(ndvi1)
    biomass2 = estimate_biomass(ndvi2)

    return {
        "biomass_t1": biomass1,
        "biomass_t2": biomass2,
        "biomass_change": biomass2 - biomass1
    }