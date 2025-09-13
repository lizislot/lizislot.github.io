# Complex Analysis Notes


This page summarizes key topics in complex analysis I have studied.
The textbook recommended: Fundamentals of Complex Analysis by E.B Saff A.D. Snider 3th ed

---

## 1. Complex Numbers and Complex Plane
- Basic operations: addition, subtraction, multiplication, division
- Representation in complex plane
- Keywords: 复数运算, 复平面

---

## 2. Exponential of Complex Numbers
- For z = x + iy, e^z = e^x (cos y + i sin y)
- Euler's formula: e^{iθ} = cos θ + i sin θ
- Keywords: 指数, 欧拉公式

---

## 3. Riemann Sphere and Stereographic Projection
- Map complex plane to sphere
- Extended complex plane (∞ included)
- Keywords: 黎曼球, 立体投影

---

## 4. Limits and Continuity of Complex Functions
- Limit: lim_{z→z0} f(z)
- Continuity definition similar to real functions
- Keywords: 极限, 连续

---

## 5. Analytic Functions
- Function is analytic if it is differentiable everywhere in its domain
- Keywords: 解析函数, 处处可导

---

## 6. Cauchy-Riemann Equations
- ∂u/∂x = ∂v/∂y, ∂u/∂y = -∂v/∂x for f(z) = u(x,y) + i v(x,y)
- Keywords: 柯西-黎曼方程

---

## 7. Harmonic Functions
- If f is analytic, its real part u(x,y) and imaginary part v(x,y) are harmonic:
  ∇²u = 0, ∇²v = 0
- Keywords: 调和函数

---

## 8. Trigonometric Functions of Complex Variables
- sin z = (e^{iz} - e^{-iz}) / (2i)
- cos z = (e^{iz} + e^{-iz}) / 2
- Keywords: 复三角函数, 欧拉公式

---

## 9. Cauchy Integral Formula
- f(a) = (1/2πi) ∮_C f(z)/(z-a) dz
- Applications: evaluation of integrals, derivatives
- Keywords: 柯西积分公式

---

## 10. Generalized Cauchy Integral Formula
- If f is analytic inside a positively oriented contour γ and z is inside γ:
  
  f^{(n)}(z) = (n! / 2πi) ∮_γ f(τ) / (τ - z)^{n+1} dτ
- Keywords: 半导铁盒公式 (general form)

---

## 11. Cauchy Estimates
- If f is analytic inside and on a circle C_R centered at z0 with radius R,
  and |f(z)| ≤ M, then:
  
  \|(f^{(n)}(z0))\| ≤ (n! M) / R^n
- Keywords: 柯西估计

---

## 12. Liouville’s Theorem and Maximum Modulus Principle
- Liouville: A bounded entire function must be constant
- Maximum modulus principle: \|(f(z))\| achieves maximum only on boundary
- Keywords: 刘维尔定理, 最大值定理, harmonic function

---

## 13. Convergence of Series
- Ratio test for convergence
- Cauchy criterion for convergence
- Keywords: 数列收敛, ratio test, Cauchy 法

---

## 14. Taylor Series Expansion
- Expansion of analytic functions in power series around a point
- Keywords: 泰勒级数, 复平面展开

---

## 15. Laurent Series Expansion
- Expansion including negative powers, valid in annulus
- Keywords: Laurent 级数

---

## 16. Singularities
- Classification: removable, pole, essential
- Keywords: 奇点

---

## 17. Residues and Residue Theorem
- Residue at isolated singularity
- Residue theorem: ∮_C f(z) dz = 2πi Σ Residues inside C
- Keywords: 留数, 留数定理
