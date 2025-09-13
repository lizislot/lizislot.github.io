<style>
body {
    background: #1e1e1e;   /* 深色背景 */
    color: #f5f5f5;        /* 白灰字体 */
    font-size: 18px;
    line-height: 1.8;
    margin: 0 auto;
    max-width: 900px;
    padding: 2rem;
}
h1, h2, h3 {
    color: #4db8ff;
}
a { color: #66ccff; }
code, pre {
    background: #2d2d2d;
    color: #f8f8f2;
    padding: 0.3rem 0.6rem;
    border-radius: 6px;
}
</style>

# Abstract Algebra Notes


This page summarizes fundamental concepts in abstract algebra.  

---

## 1. Groups (群)
- A group (G, *) satisfies:  
  1. Closure: a*b ∈ G  
  2. Associativity: (a*b)*c = a*(b*c)  
  3. Identity: ∃ e ∈ G such that e*a = a*e = a  
  4. Inverses: ∀a ∈ G, ∃ a⁻¹ such that a*a⁻¹ = e  
- Keywords: 群, group

---

## 2. Rings (环)
- A ring (R, +, ·) is a set with:  
  - (R, +) is an abelian group  
  - (R, ·) is associative  
  - Distributive law: a·(b+c) = a·b + a·c  
- Keywords: 环, ring

---

## 3. Symmetric Groups (对称群)
- Symmetric group Sₙ = group of all permutations on n elements  
- Order = n!  
- Keywords: 对称群, permutation group

---

## 4. Lagrange’s Theorem (拉格朗日定理)
- If H is a subgroup of finite group G, then |H| divides |G|  
- Keywords: 拉格朗日定理, 子群

---

## 5. Fermat’s Little Theorem (小费马定理)
- If p is prime and a ∉ pℤ, then a^{p-1} ≡ 1 (mod p)  
- Keywords: 小费马, 素数

---

## 6. Ideals (理想)
- An ideal I of a ring R:  
  - Closed under addition  
  - Closed under multiplication by any r ∈ R  
- Used to define quotient rings  
- Keywords: 理想, quotient ring

---

## 7. Fields (域)
- A field is a commutative ring with 1, in which every nonzero element has a multiplicative inverse  
- Examples: ℚ, ℝ, ℂ, finite fields 𝔽ₚ  
- Keywords: 域, field
