import numpy as np

def get_satellite_image(time_step):
    """
    Simulated satellite image:
    channels = [red, green, blue, nir]
    """

    np.random.seed(time_step)

    image = np.random.rand(4, 256, 256)

    red = image[0]
    nir = image[3]

    return red, nir