# Discrete Mathematics Notes

This page summarizes key concepts in discrete mathematics.  
The textbook recommended: Applied Combinatorics by Alan Tucker 6th ed

---

## 1. Graph Isomorphism
- Two graphs G₁ and G₂ are isomorphic if there exists a bijection between vertices preserving adjacency  
- Keywords: 同构, 图

---

## 2. Graphs and Directed Graphs
- Graph G = (V, E), edges can be undirected or directed  
- Directed graph = digraph  
- Keywords: 图, 有向图

---

## 3. Planar Graphs and Special Graphs
- Planar graph: can be drawn without edge crossings  
- Bipartite graph: vertices can be partitioned into two sets, edges across sets only  
- Complete graph Kₙ: every pair of distinct vertices connected  
- Keywords: 平面图, 二部图, 完全图

---

## 4. Euler’s Formula
- For connected planar graphs:  
  r = e - v + 2  
  where r = number of regions, e = edges, v = vertices  
- Keywords: 欧拉公式, 面

---

## 5. Euler Cycles and Hamilton Circuits
- Euler cycle: uses every edge exactly once  
- Hamilton circuit: visits every vertex exactly once  
- Keywords: 欧拉回路, 哈密顿回路

---

## 6. Hamilton Circuit Criterion
- Dirac’s Theorem: If every vertex has degree ≥ n/2, then G has a Hamiltonian circuit  
- Keywords: 哈密顿判定, Dirac

---

## 7. Graph Coloring
- Assign colors to vertices so adjacent vertices have different colors  
- Chromatic number χ(G): minimum number of colors needed  
- Keywords: 染色问题

---

## 8. Trees and Spanning Trees
- Tree: connected, acyclic graph  
- Search trees: binary search tree, depth-first, breadth-first  
- Minimum spanning trees: Kruskal’s and Prim’s algorithms  
- Keywords: 树, 最小生成树, 搜索树

---

## 9. Shortest Paths
- Dijkstra’s algorithm for weighted graphs  
- Bellman-Ford algorithm for graphs with negative weights  
- Keywords: 最短路径

---

## 10. Network Flows
- Maximum flow problem  
- Ford-Fulkerson algorithm  
- Keywords: 网络流

---

## 11. Matchings and Hall’s Marriage Theorem
- Matching: set of edges without common vertices  
- Hall’s Marriage Theorem: A bipartite graph G=(X,Y,E) has a matching covering X iff \|N(S)\| ≥ \|S\| for all S ⊆ X  
- Keywords: 匹配, 婚姻定理

---

## 12. Combinations and Permutations
- See probability notes for formulas  
- Keywords: 排列组合

---

## 13. Generating Functions
- Useful for counting sequences and solving recurrences  
- Ordinary generating function: G(x) = Σ aₙ xⁿ  
- Keywords: 生成函数

---

## 14. Recurrence Relations
- Linear recurrence: aₙ = c₁aₙ₋₁ + ... + cₖaₙ₋ₖ  
- Solve using characteristic equations  
- Keywords: 递推关系

---

## 15. Inclusion–Exclusion Principle
- Same as in probability  
- Used in combinatorial counting  
- Keywords: 容斥原理
