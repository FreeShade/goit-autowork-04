def prepare_data(data):
    data = sorted(data)
    data.pop(0) and data.pop(-1)

    return sorted(data)
