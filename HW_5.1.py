def distance(x1, y1, x2, y2):
    distanceBetweenPoints = (((x2-x1)**2)+((y2-y1)**2))**0.5
    return round(distanceBetweenPoints, 2)