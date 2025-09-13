# Real Analysis Notes

This page summarizes fundamental concepts in real analysis.  
The textbook recommended: Real Analysis by Jay Cummings 2nd ed
                        and Taozhexuan's real Analysis 陶哲轩实分析 

---

## 1. Cardinality
- Countable vs. uncountable sets  
- Examples: ℕ (countable), ℝ (uncountable)  
- Keywords: 基数

---

## 2. Sequences and Convergence
- Definition: {a_n} → L if ∀ε>0, ∃N s.t. |a_n - L| < ε when n > N  
- Keywords: 数列, 收敛

---

## 3. Comparison Test
- If 0 ≤ a_n ≤ b_n and ∑ b_n converges, then ∑ a_n also converges  
- Keywords: 比较判别法

---

## 4. p-Series Test
- ∑ (1/n^p) converges if p > 1, diverges if p ≤ 1  
- Keywords: p-级数

---

## 5. Absolute Convergence
- If ∑ |a_n| converges, then ∑ a_n also converges  
- Keywords: 绝对收敛

---

## 6. Rearrangement Theorem
- Absolutely convergent series: any rearrangement converges to same sum  
- Conditionally convergent series: rearrangements may change the limit  
- Keywords: 重排定理

---

## 7. Closed Sets
- A set is closed iff it contains all its limit points  
- Keywords: 闭集, 极限点

---

## 8. Compactness
- Heine–Borel theorem: In ℝ^n, compact ⇔ closed + bounded  
- Equivalent definition: every open cover has a finite subcover  
- Keywords: 紧致, 有界

---

## 9. Function Limits and Squeeze Theorem
- Limit definition for functions: lim_{x→a} f(x) = L  
- Squeeze theorem: if g(x) ≤ f(x) ≤ h(x) and lim g = lim h = L, then lim f = L  
- Keywords: 函数极限, 夹逼定理

---

## 10. Continuity
- f is continuous at a if lim_{x→a} f(x) = f(a)  
- Keywords: 连续

---

## 11. Extreme Value Theorem
- A continuous function on a compact set attains maximum and minimum  
- Keywords: 极值定理

---

## 12. Uniform Continuity
- f is uniformly continuous on A if ∀ε>0, ∃δ>0 such that |x-y|<δ ⇒ |f(x)-f(y)|<ε for all x,y∈A  
- Stronger than pointwise continuity  
- Keywords: 一致连续
