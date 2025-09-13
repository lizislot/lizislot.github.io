# Fourier Analysis Notes

This page summarizes the key concepts in Fourier analysis.  

---

## 1. Fourier Series (傅里叶级数)
- Represent periodic functions as sums of sines and cosines  
- Formula: f(x) = a₀/2 + Σ (aₙ cos(nx) + bₙ sin(nx))  
- Convergence conditions: Dirichlet conditions  
- Keywords: 傅里叶级数, 周期函数

---

## 2. Fourier Transform (傅里叶变换)
- Representation of a function in frequency domain  
- Definition: F(ω) = ∫ f(t) e^{-iωt} dt  
- Inverse transform recovers f(t)  
- Keywords: 傅里叶变换, 频域

---

## 3. L² Space and Hilbert Spaces (L² 与希尔伯特空间)
- L²(ℝ): space of square-integrable functions  
- Hilbert space: complete inner product space  
- Orthogonality of sine and cosine functions in L²  
- Keywords: L²空间, 希尔伯特空间

---

## 4. Inner Products and Convolution (内积与卷积)
- Inner product: ⟨f,g⟩ = ∫ f(x) g̅(x) dx  
- Convolution: (f * g)(t) = ∫ f(τ) g(t-τ) dτ  
- Fourier transform converts convolution into multiplication  
- Keywords: 内积, 卷积

---

## 5. Generalized Orthogonal Bases and Dot Product (广义正交基与点乘)
- Functions {φₙ} form orthogonal basis if ⟨φₙ, φₘ⟩ = 0 for n≠m  
- Generalization beyond trigonometric functions (e.g., wavelets)  
- Keywords: 正交基, 点积

---

## 6. Convolution Kernels (卷积核)
- Examples:  
  - Box kernel (moving average)  
  - Gaussian kernel (smoothing)  
  - Delta function (identity kernel)  
- Used in signal processing and PDEs  
- Keywords: 卷积核, 信号处理
