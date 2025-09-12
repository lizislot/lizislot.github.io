# My Mathematics Notes and Theorems

Welcome to my personal mathematics reference page. Here I summarize key concepts, theorems, and results I have studied.

---
## 1. Calculus. The textbook recommended Calculus by James stewart 
## 1. Differential Calculus and Plotting
- Derivatives, higher order derivatives
- Plotting functions to analyze behavior
- Keywords: 微积分, 绘图

---

## 2. Optimization Problems 
- Critical points, second derivative test
- Constrained optimization using Lagrange multipliers
- Keywords: 极值, 拉格朗日乘子

---

## 3. Limits and Asymptotes
- Limits as x → a or x → ∞
- Horizontal, vertical, oblique asymptotes
- Keywords: 极限, 渐近线

---

## 4. Riemann Sums and Riemann Integrals
- Approximating area under curves using sums
- Definition of definite integral
- Keywords: 黎曼和, 黎曼积分

---

## 5. The Midpoint Rule
- Numerical integration using midpoint approximation
- Keywords: 中点法

---

## 6. The Mean Value Theorem
- If f is continuous on [a,b] and differentiable on (a,b), then f'(c) = (f(b)-f(a))/(b-a)
- Keywords: 中值定理

---

## 7. Integration by Parts
- ∫ u dv = uv - ∫ v du
- Keywords: 积分分部法

---

## 8. Euler's Method
- Numerical solution of ODEs
- Keywords: 欧拉法

---

## 9. Taylor / Maclaurin Series
- f(x) = f(a) + f'(a)(x-a) + f''(a)/2!(x-a)^2 + ...
- Keywords: 泰勒展开, 麦克劳林

---

## 10. Vector Space: Dot Product and Cross Product
- Dot product: a·b = |a||b|cosθ
- Cross product: a × b gives a vector perpendicular to a and b
- Keywords: 向量, 点乘, 叉乘

---

## 11. Common Sphere Equations in n-Dimensional Space
- Equation: (x1-a1)^2 + (x2-a2)^2 + ... + (xn-an)^2 = r^2
- Keywords: n维, Sphere, 方程

---

## 12. Multivariable Calculus Operations
- Partial derivatives, gradient, directional derivative
- Keywords: 偏导数, 梯度

---

## 13. Lagrange Multipliers
- Solve constrained optimization problems: ∇f = λ∇g
- Keywords: 拉格朗日乘子

---

## 14. Changing the Order of Integration
- Double/triple integrals: ∫∫ f(x,y) dxdy = ∫∫ f(x,y) dydx
- Keywords: 积分换序

---

## 15. 3D Coordinates and Spherical / Polar Coordinates
- Cartesian (x,y,z) ↔ Spherical (ρ,θ,φ)
- Keywords: 三维坐标, 球坐标, 极坐标

---

## 16. Gradient, Divergence, Curl
- ∇f, ∇·F, ∇×F
- Gradient of scalar, divergence and curl of vector field
- Keywords: 梯度, 散度, 旋度

---

## 17. Green's Theorem and Stokes' Theorem
- Green: ∮C F·dr = ∬R (∂N/∂x - ∂M/∂y) dA
- Stokes: ∮∂S F·dr = ∬S (∇×F)·dS
- Keywords: 格林公式, 斯托克斯公式

---

## 2.linear algebra the textbook recommended Linear Algebra by Stephen H. Friedberg
## 1. Vector Spaces and Subspaces
- Definition of vector spaces and subspaces
- Examples: R^n, function spaces
- Keywords: 向量空间, 子空间

---

## 2. Gaussian Elimination
- Solve linear systems using row operations
- Reduced row echelon form
- Keywords: 高斯消元法, 方程求解

---

## 3. Linear Independence, Span, and Basis
- Linear independence of vectors
- Span of a set of vectors
- Basis of a vector space
- Keywords: 线性无关, 张成, 基

---

## 4. Dimension, Kernel, and Rank
- Dimension of vector space
- Kernel (null space) of a linear transformation or matrix
- Rank of a matrix
- Keywords: 维度, 核, 秩

---

## 5. Dimension Theorem
- For linear map T: V → W, dim(V) = dim(ker(T)) + dim(im(T))
- Keywords: 维数定理, 线性映射

---

## 6. Matrix Inverse and Determinant
- Conditions for invertibility
- Determinant calculation and properties
- Keywords: 矩阵逆, 行列式

---

## 7. Eigenvalues and Eigenvectors
- Definition and characteristic equation: det(A - λI) = 0
- Diagonalization: A = PDP⁻¹
- Keywords: 特征值, 特征向量
---

## 3. Complex Analysis Notes
# 复变函数笔记（关键词保留中文）

This page summarizes key topics in complex analysis I have studied.
本页面总结了我学习的复变函数的关键知识点。

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
  
  |f^{(n)}(z0)| ≤ (n! M) / R^n
- Keywords: 柯西估计

---

## 12. Liouville’s Theorem and Maximum Modulus Principle
- Liouville: A bounded entire function must be constant
- Maximum modulus principle: |f(z)| achieves maximum only on boundary
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

---

## 4. Selected Theorems
- **Cauchy-Schwarz Inequality:** \(|\langle x, y \rangle| \leq \|x\| \|y\|\)
- **Bayes' Theorem:** \(P(A|B) = \frac{P(B|A)P(A)}{P(B)}\)
- **Taylor's Theorem:** \(f(x) = f(a) + f'(a)(x-a) + \frac{f''(\xi)}{2!}(x-a)^2, \xi \in (a,x)\)

---

## 5. Notes / Remarks
- Each section can be expanded with examples and proofs.
- I will continue updating this page as I study more topics.
