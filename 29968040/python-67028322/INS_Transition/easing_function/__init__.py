from .cubic_bezier import CubicBezier
import re


# 预定义的缓动函数
linear = CubicBezier(0.0, 0.0, 1.0, 1.0)
ease = CubicBezier(0.25, 0.1, 0.25, 1.0)
ease_in = CubicBezier(0.42, 0.0, 1.0, 1.0)
ease_out = CubicBezier(0.0, 0.0, 0.58, 1.0)
ease_in_out = CubicBezier(0.42, 0.0, 0.58, 1.0)

# 预定义缓动函数的映射字典
PREDEFINED_EASING = {
    'linear': linear,
    'ease': ease,
    'ease-in': ease_in,
    'ease-out': ease_out,
    'ease-in-out': ease_in_out
}


def is_easing_function(data):
    return isinstance(data, CubicBezier)


def parse_easing_function(easing_function):
    """解析 css 格式的缓动函数"""
    if is_easing_function(easing_function):
        return easing_function

    if isinstance(easing_function, str):
        # 处理 cubic-bezier 格式
        if easing_function.startswith('cubic-bezier'):
            # 匹配括号内的数字序列
            match = re.search(r'cubic-bezier\(([^)]+)\)', easing_function)
            if not match:
                raise ValueError(f"无效的 cubic-bezier 格式: {easing_function}")

            # 解析数字
            numbers_str = match.group(1)
            try:
                # 安全地解析数字序列
                numbers = [float(num.strip()) for num in numbers_str.split(',')]
            except ValueError as exc:
                raise ValueError(f"无法解析 cubic-bezier 参数: {numbers_str}") from exc

            if len(numbers) != 4:
                raise ValueError(f"cubic-bezier 需要4个参数，但得到 {len(numbers)} 个")

            return CubicBezier(*numbers)

        # 处理预定义的缓动函数名称
        if easing_function in PREDEFINED_EASING:
            return PREDEFINED_EASING[easing_function]

    raise ValueError(f"无法解析此格式: {easing_function}")