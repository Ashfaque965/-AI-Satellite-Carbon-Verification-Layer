def biomass_to_co2(biomass_tons):
    return biomass_tons * 0.47 * 3.67


def calculate_carbon_credits(old_biomass, new_biomass):

    delta = new_biomass - old_biomass

    # prevent negative credit fraud
    if delta <= 0:
        return 0

    return biomass_to_co2(delta)


def mrv_confidence(delta_ndvi):
    """
    Simple uncertainty proxy
    """

    if abs(delta_ndvi) < 0.02:
        return 0.4
    elif abs(delta_ndvi) < 0.1:
        return 0.7
    else:
        return 0.95