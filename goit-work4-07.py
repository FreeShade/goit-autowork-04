points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if len(coordinates) <= 1:
        return 0
    distance = 0
    for i in range(len(coordinates) - 1):
        if coordinates[i] < coordinates[i + 1]:
            key = (coordinates[i], coordinates[i + 1])
        else:
            key = (coordinates[i + 1], coordinates[i])
        distance += points[key]
    return distance
