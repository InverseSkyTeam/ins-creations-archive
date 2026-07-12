def clampLng(lng):
    return ((lng + 180) % 360) - 180


def clamp(x, _min, _max):
    return _min if x < _min else (_max if x > _max else x)


def ease_in_out_cubic(x):
    return 4 * x * x * x if x < 0.5 else 1 - pow(-2 * x + 2, 3) / 2

