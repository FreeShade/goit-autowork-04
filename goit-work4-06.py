def split_list(lst):
    if not lst:
        return [], []

    avg = sum(lst) / len(lst)

    lower = [num for num in lst if num <= avg]  #
    higher = [num for num in lst if num > avg]

    return lower, higher
