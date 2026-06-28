import json

def load_geojson(path: str):
    with open(path, "r") as f:
        return json.load(f)


def get_bbox(geojson_feature):
    """
    Extract bounding box from GeoJSON polygon
    (simplified MVP version)
    """

    coords = geojson_feature["geometry"]["coordinates"][0]

    lons = [c[0] for c in coords]
    lats = [c[1] for c in coords]

    return {
        "min_lon": min(lons),
        "max_lon": max(lons),
        "min_lat": min(lats),
        "max_lat": max(lats)
    }