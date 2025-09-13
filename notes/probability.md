# Probability Theory Notes

This page summarizes key concepts in probability theory.  
The textbook recommended: A First Course in Probability by Sheldon Ross 10th ed

---

## 1. Permutations and Combinations
- Permutations: number of ways to arrange n objects  
  P(n, r) = n! / (n-r)!  
- Combinations: number of ways to choose r objects  
  C(n, r) = n! / (r!(n-r)!)  
- Keywords: 排列, 组合

---

## 2. Probability as Measure of Belief
- Axiomatic definition: P(Ω) = 1, 0 ≤ P(A) ≤ 1, countable additivity  
- Frequentist vs Bayesian interpretations  
- Keywords: 概率, 信念测度

---

## 3. Conditional Probability
- P(A|B) = P(A ∩ B) / P(B), if P(B) > 0  
- Keywords: 条件概率

---

## 4. Bayes’ Theorem
- P(A|B) = [P(B|A) P(A)] / P(B)  
- Applications: medical testing, machine learning  
- Keywords: 贝叶斯公式

---

## 5. Independence and Correlation
- Independent events: P(A ∩ B) = P(A)P(B)  
- Independence of random variables  
- Correlation measures linear relationship: ρ(X,Y) = Cov(X,Y) / (σ_X σ_Y)  
- Keywords: 独立性, 相关性

---

## 6. Common Distributions
- **Discrete:**  
  - Bernoulli(p)  
  - Binomial(n, p)  
  - Poisson(λ)  
  - Geometric(p)  
  - Negative Binomial(r, p)  
  - Hypergeometric(N, K, n)  

- **Continuous:**  
  - Uniform(a, b)  
  - Exponential(λ)  
  - Gamma(α, β)  
  - Weibull(k, λ)  
  - Beta(α, β)  
  - Pareto(α, x_m)  
  - Normal(μ, σ²)  

- Keywords: 分布, 伯努利, 二项分布, 泊松, 几何, 指数, 正态

---

## 7. Jointly Distributed Random Variables
- Joint distribution function: F(x,y) = P(X ≤ x, Y ≤ y)  
- Independence: f(x,y) = f_X(x) f_Y(y)  
- Covariance and correlation  
- Keywords: 联合分布, 随机变量

---

## 8. Moment Generating Functions and Variance
- MGF: M_X(t) = E[e^{tX}]  
- Variance: Var(X) = E[X²] - (E[X])²  
- Law of Total Variance: Var(X) = E[Var(X|Y)] + Var(E[X|Y])  
- Keywords: 矩母函数, 方差公式, 完全方差公式

---

## 9. A Note on Statistics
- While statistics is often treated separately, it builds on probability theory  
- Topics include estimation, hypothesis testing, confidence intervals, regression  
- Keywords: 统计, 应用

---

## 10. Inclusion–Exclusion Principle
- For two sets: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)  
- General form for n sets:  
  P(∪ A_i) = Σ P(A_i) - Σ P(A_i ∩ A_j) + Σ P(A_i ∩ A_j ∩ A_k) - ...  
- Applications: counting problems, probability of at least one event  
- Keywords: 容斥原理
