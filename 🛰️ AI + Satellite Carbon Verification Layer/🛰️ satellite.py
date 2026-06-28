import numpy as np

def get_satellite_image(time_step: int):
    """
    Simulated satellite image with 4 bands:
    [red, green, blue, nir]
    """

    np.random.seed(time_step)

    image = np.random.rand(4, 256, 256)

    red = image[0]
    nir = image[3]

    return red, nir