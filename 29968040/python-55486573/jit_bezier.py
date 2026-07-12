import math
import sys
import numpy as np
try:
    from numba.experimental import jitclass
except ImportError:
    from numba import jitclass
from numba import njit, float64


np.seterr(divide='ignore')


kMaxNewtonIterations = 4  # 最大牛顿迭代次数
kBezierEpsilon = 1e-7
CUBIC_BEZIER_SPLINE_SAMPLES = 11
FLOAT_MAX = sys.float_info.max
FLOAT_MIN = -sys.float_info.max


@njit('float64(float64, float64, float64)')
def clamp(x, _min, _max):
    return _min if x < _min else (_max if x > _max else x)


@njit('float64(float64, float64)')
def my_divide(a, b):
    return np.divide(a, b)


spec = [
    ('ax_', float64), ('bx_', float64), ('cx_', float64),
    ('ay_', float64), ('by_', float64), ('cy_', float64),
    ('start_gradient_', float64), ('end_gradient_', float64),
    ('range_min_', float64), ('range_max_', float64),
    ('spline_samples_', float64[:])
]


@jitclass(spec)
class CubicBezier:
    def __init__(self, p1x, p1y, p2x, p2y):
        self.ax_ = self.bx_ = self.cx_ = 0
        self.ay_ = self.by_ = self.cy_ = 0
        self.start_gradient_ = self.end_gradient_ = 0
        self.range_min_ = self.range_max_ = 0
        self.spline_samples_ = np.zeros(CUBIC_BEZIER_SPLINE_SAMPLES, dtype=np.float64)

        self.InitCoefficients(p1x, p1y, p2x, p2y)
        self.InitGradients(p1x, p1y, p2x, p2y)
        self.InitRange(p1y, p2y)
        self.InitSpline()

    def SampleCurveX(self, t: float64) -> float64:
        return ((self.ax_ * t + self.bx_) * t + self.cx_) * t

    def SampleCurveY(self, t: float64) -> float64:
        return self.ToFinite(((self.ay_ * t + self.by_) * t + self.cy_) * t)

    def SampleCurveDerivativeX(self, t: float64) -> float64:
        return (3.0 * self.ax_ * t + 2.0 * self.bx_) * t + self.cx_

    def SampleCurveDerivativeY(self, t: float64) -> float64:
        return self.ToFinite(
            self.ToFinite(self.ToFinite(3.0 * self.ay_) * t + self.ToFinite(2.0 * self.by_)) * t + self.cy_)

    @staticmethod
    def GetDefaultEpsilon() -> float64:
        return kBezierEpsilon

    def SolveCurveX(self, x: float64, epsilon: float64) -> float64:
        assert 0 <= x <= 1
        t0 = t1 = 0
        t2 = x
        x2 = d2 = 0

        # 对样条曲线进行线性插值以获取初始猜测
        delta_t = 1.0 / (CUBIC_BEZIER_SPLINE_SAMPLES - 1)
        for i in range(CUBIC_BEZIER_SPLINE_SAMPLES):
            if x <= self.spline_samples_[i]:
                t1 = delta_t * i
                t0 = t1 - delta_t
                t2 = t0 + (t1 - t0) * (x - self.spline_samples_[i - 1]) / \
                                      (self.spline_samples_[i] - self.spline_samples_[i - 1])
                break

        # 先进行牛顿迭代法
        newton_epsilon = min(kBezierEpsilon, epsilon)
        for i in range(kMaxNewtonIterations):
            x2 = self.SampleCurveX(t2) - x
            if abs(x2) < newton_epsilon:  # 精度足够
                return t2
            d2 = self.SampleCurveDerivativeX(t2)
            if abs(d2) < kBezierEpsilon:
                break
            t2 = t2 - x2 / d2

        if abs(x2) < epsilon:
            return t2

        # 如果牛顿迭代法没有收敛，那么使用二分计算
        while t0 < t1:
            x2 = self.SampleCurveX(t2)
            if abs(x2 - x) < epsilon:
                return t2
            if x > x2:
                t0 = t2
            else:
                t1 = t2
            t2 = (t1 + t0) * 0.5

        return t2

    def Solve(self, x: float64) -> float64:
        return self.SolveWithEpsilon(x, kBezierEpsilon)

    def SolveWithEpsilon(self, x: float64, epsilon: float64) -> float64:
        if x < 0.0:
            return self.ToFinite(0.0 + self.start_gradient_ * x)
        if x > 1.0:
            return self.ToFinite(1.0 + self.end_gradient_ * (x - 1.0))
        return self.SampleCurveY(self.SolveCurveX(x, epsilon))

    def Slope(self, x: float64) -> float64:
        return self.SlopeWithEpsilon(x, kBezierEpsilon)

    def SlopeWithEpsilon(self, x: float64, epsilon: float64) -> float64:
        x = clamp(x, 0.0, 1.0)
        t = self.SolveCurveX(x, epsilon)
        dx = self.SampleCurveDerivativeX(t)
        dy = self.SampleCurveDerivativeY(t)
        if not dx and not dy:
            return 0
        return self.ToFinite(my_divide(dy, dx))

    def GetX1(self) -> float64:
        return self.cx_ / 3.0

    def GetY1(self) -> float64:
        return self.cy_ / 3.0

    def GetX2(self) -> float64:
        return (self.bx_ + self.cx_) / 3.0 + self.GetX1()

    def GetY2(self) -> float64:
        return (self.by_ + self.cy_) / 3.0 + self.GetY1()

    def range_min(self) -> float64:
        return self.range_min_

    def range_max(self) -> float64:
        return self.range_max_

    def InitCoefficients(self, p1x: float64, p1y: float64, p2x: float64, p2y: float64) -> float64:
        self.cx_ = 3.0 * p1x
        self.bx_ = 3.0 * (p2x - p1x) - self.cx_
        self.ax_ = 1.0 - self.cx_ - self.bx_

        self.cy_ = self.ToFinite(3.0 * p1y)
        self.by_ = self.ToFinite(3.0 * (p2y - p1y) - self.cy_)
        self.ay_ = self.ToFinite(1.0 - self.cy_ - self.by_)

    def InitGradients(self, p1x: float64, p1y: float64, p2x: float64, p2y: float64) -> float64:
        if p1x > 0:
            self.start_gradient_ = p1y / p1x
        elif not p1y and p2x > 0:
            self.start_gradient_ = p2y / p2x
        elif not p1y and not p2y:
            self.start_gradient_ = 1
        else:
            self.start_gradient_ = 0

        if p2x < 1:
            self.end_gradient_ = (p2y - 1) / (p2x - 1)
        elif p2y == 1 and p1x < 1:
            self.end_gradient_ = (p1y - 1) / (p1x - 1)
        elif p2y == 1 and p1y == 1:
            self.end_gradient_ = 1
        else:
            self.end_gradient_ = 0

    def InitRange(self, p1y: float64, p2y: float64) -> float64:
        self.range_min_ = 0
        self.range_max_ = 1
        if 0 <= p1y < 1 and 0 <= p2y <= 1:
            return

        epsilon = kBezierEpsilon

        a = 3.0 * self.ay_
        b = 2.0 * self.by_
        c = self.cy_

        if abs(a) < epsilon and abs(b) < epsilon:
            return

        t1 = 0
        t2 = 0

        if abs(a) < epsilon:
            t1 = my_divide(-c, b)
        else:
            discriminant = b * b - 4 * a * c
            if discriminant < 0:
                return
            discriminant_sqrt = math.sqrt(discriminant)
            t1 = my_divide((-b + discriminant_sqrt), (2 * a))
            t2 = my_divide((-b - discriminant_sqrt), (2 * a))

        sol1 = 0
        sol2 = 0

        if 0 < t1 < 1:
            sol1 = self.SampleCurveY(t1)

        if 0 < t2 < 1:
            sol2 = self.SampleCurveY(t2)

        self.range_min_ = min(self.range_min_, sol1, sol2)
        self.range_max_ = max(self.range_max_, sol1, sol2)

    def InitSpline(self) -> float64:
        delta_t = 1.0 / (CUBIC_BEZIER_SPLINE_SAMPLES - 1)
        for i in range(CUBIC_BEZIER_SPLINE_SAMPLES):
            self.spline_samples_[i] = self.SampleCurveX(i * delta_t)

    @staticmethod
    def ToFinite(value: float64) -> float64:
        if math.isinf(value):
            if value > 0:
                return FLOAT_MAX
            return FLOAT_MIN
        return value
