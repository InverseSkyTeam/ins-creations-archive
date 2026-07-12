def clamp(value, minimum, maximum):
    # 判断给定的value是否在区间（minimum, maximum）中
    if minimum == maximum:
        return minimum
    if minimum > maximum:
        raise ValueError("minimum is greater than maximum.")
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value