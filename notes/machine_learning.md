# Machine Learning Notes

This page summarizes basic concepts and algorithms in machine learning.  
The textbook recommended: 

The Elements of Statistical Learning: Data mining, Inference, and Prediction 2nd 3d
By Trevor Hastie, Robert Tibshirani, Jerome Friedman 

An Introduction to Statistical Learning 2nd ed
By Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani

Pattern Recognition and Machine Learning by Christopher M.Bishop

---

## 1. Least Squares (最小二乘)
- Method to minimize the sum of squared residuals  
- Used in regression problems  
- Keywords: 最小二乘, approximation

---

## 2. Linear Regression (线性回归)
- Model: y = β₀ + β₁x + ε  
- Fit by minimizing squared errors  
- Keywords: 线性回归, supervised learning

---

## 3. Logistic Regression (逻辑回归)
- Used for classification (binary outcomes)  
- Model: P(y=1\|x) = 1 / (1 + e^{-(β₀ + β₁x)})  
- Keywords: 分类, logistic function

---

## 4. K-Nearest Neighbors (KNN)
- Non-parametric method  
- Classify a point based on majority vote among k nearest neighbors  
- Keywords: 最近邻, non-parametric

---

## 5. K-Fold Cross Validation (K折交叉验证)
- Split dataset into k parts, train on k-1 parts, validate on the rest  
- Repeat k times, average the performance  
- Keywords: 模型验证, 减少过拟合

---

## 6. Principal Component Analysis (PCA)
- Dimensionality reduction method  
- Projects data onto directions of maximum variance  
- Keywords: 主成分分析, 降维

---

## 7. Decision Trees (决策树)
- Tree-based model for classification and regression  
- Split data based on feature thresholds  
- Keywords: 树模型, 可解释性

---

## 8. Support Vector Machine (SVM 支持向量机)
- Finds hyperplane that maximizes margin between classes  
- Can use kernel trick for non-linear data  
- Keywords: 支持向量机, 分类, kernel method
