def game(terra, power):
    for sublist in terra:
        for val in sublist:
            if val <= power:
                power = power + val
            else:
                break
    return power
