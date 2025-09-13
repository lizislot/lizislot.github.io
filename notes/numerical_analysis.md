# Numerical Analysis Notes

This page summarizes key methods and concepts in numerical analysis.  

---

## 1. Bisection Method (二分法)
- Iterative method for finding roots of f(x)=0 in [a,b]  
- Requires f(a)·f(b) < 0  
- Converges linearly  
- Keywords: 二分法, root finding

---

## 2. Newton’s Method (牛顿法)
- Iterative formula: x_{n+1} = x_n - f(x_n)/f'(x_n)  
- Quadratic convergence near the root if f’(x) ≠ 0  
- Requires differentiability  
- Keywords: 牛顿法, 快速收敛

---

## 3. Secant Method (割线法)
- Uses two initial points (x₀, x₁)  
- Formula: x_{n+1} = x_n - f(x_n)(x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))  
- Convergence rate ≈ 1.618 (superlinear)  
- Keywords: 割线法, 不需导数

---

## 4. Fixed-Point Iteration (不动点迭代)
- Solve x = g(x) by iteration x_{n+1} = g(x_n)  
- Convergence if \|g’(x*)\| < 1 at fixed point x*  
- Keywords: 不动点, 迭代收敛条件

---

## 5. LU Decomposition (LU分解)
- Factor A = LU, where L = lower triangular, U = upper triangular  
- Used for solving Ax=b efficiently  
- Keywords: LU分解, 线性方程组

---

## 6. Lagrange Interpolation (拉格朗日插值法)
- Given n+1 data points (x_i, y_i), construct polynomial:  
  P(x) = Σ y_i L_i(x), with L_i(x) = Π (x - x_j)/(x_i - x_j) for j≠i  
- Keywords: 插值, 多项式

---

## 7. Error Analysis (误差分析)
- Types: absolute error, relative error, truncation error, rounding error  
- Stability: algorithm’s sensitivity to input error  
- Keywords: 误差, 稳定性

---

## 8. Numerical Integration (数值积分)
- Trapezoidal rule: approximate with trapezoids  
- Simpson’s rule (辛普森积分): quadratic interpolation for accuracy  
- Euler’s method (欧拉积分): simple numerical ODE solver:  
  y_{n+1} = y_n + h f(t_n, y_n)  
- Keywords: 积分近似, ODE数值解
