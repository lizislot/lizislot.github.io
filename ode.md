# Ordinary Differential Equations (ODE)


This page summarizes key concepts and results about ODEs.
The textbook recommended: Fundamentals of Differential Equations By Nagle Sff Snider 7th ed

---

## 1. Existence and Uniqueness of Solutions
- Picard–Lindelöf theorem: under Lipschitz condition, solution exists and is unique
- Example: dy/dx = f(x, y), with initial condition y(x0) = y0
- Keywords: 解的存在性, 唯一性

---

## 2. General Solutions to Systems of ODE
- Linear system: y' = A y, where A is a matrix
- General solution form: y(t) = c1 y1(t) + c2 y2(t) + … + cn yn(t)
- Solutions related to eigenvalues/eigenvectors of A
- Keywords: 常微分方程组, 通解

---

## 3. Wronskian and Inhomogeneous Equations
- Wronskian determinant W(y1, …, yn) used to check linear independence of solutions
- For inhomogeneous linear ODE: y'' + p(x)y' + q(x)y = g(x)
  - General solution = homogeneous solution + particular solution
- Methods: undetermined coefficients, variation of parameters
- Keywords: Wronskian 行列式, 非齐次方程
