from .cubic_bezier import CubicBezier

linear = CubicBezier(0.0, 0.0, 1.0, 1.0)
ease = CubicBezier(0.25, 0.1, 0.25, 1.0)
ease_in = CubicBezier(0.42, 0.0, 1.0, 1.0)
ease_out = CubicBezier(0.0, 0.0, 0.58, 1.0)
ease_in_out = CubicBezier(0.42, 0.0, 0.58, 1.0)


def is_easing_function(data):
    if isinstance(data, (CubicBezier, )):
        return True
    return False


def parse_easing_function(easing_function):
    if is_easing_function(easing_function):
        return easing_function
    elif isinstance(easing_function, str):
        if easing_function.startswith('cubic-bezier'):
            string = easing_function[len('cubic-bezier'):]
            value = eval(string)
            assert len(value) == 4
            return CubicBezier(*[float(i) for i in value])
        elif easing_function in ('linear', 'ease', 'ease-in', 'ease-out', 'ease-in-out'):
            return eval(easing_function.replace('-', '_'))
    raise ValueError("无法解析此格式")
