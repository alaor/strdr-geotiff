import server.geotiffinfo as info


def infos():
    return {
        "filename": info.filename(),
        "cover": info.vegetationCover(),
        "area": info.area(),
        "centroid": info.centroid(),
        "local_time": "TODO"
    }
