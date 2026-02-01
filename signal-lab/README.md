# signal-lab

一个用于生成示例信号数据的 Python 项目，适合入门练习。

## 1. 创建并启用虚拟环境（venv）

在项目根目录 `signal-lab/` 下执行：

```bash
python -m venv .venv
```

- **Windows (PowerShell)**
  ```bash
  .venv\Scripts\Activate.ps1
  ```
- **macOS / Linux**
  ```bash
  source .venv/bin/activate
  ```

## 2. 安装依赖

```bash
pip install -r requirements.txt
```

> 依赖仅包含：`pandas`、`numpy`、`pytest`。

## 3. 运行命令（生成数据）

```bash
python -m signal_lab.cli --rows 200 --frequency 0.08 --noise-scale 0.03 --output output/signal.csv
```

- `--rows`：生成的行数（样本数量）
- `--frequency`：正弦波频率参数
- `--noise-scale`：噪声标准差
- `--output`：输出文件路径（默认 `output/signal.csv`）

## 4. 输出文件说明

默认会生成 `output/signal.csv`，包含以下列：

| 列名 | 含义 |
| --- | --- |
| `step` | 样本序号（从 0 开始） |
| `clean_signal` | 纯净的正弦信号（不含噪声） |
| `noise` | 随机噪声值 |
| `signal` | 叠加噪声后的最终信号 |

你可以用 Excel 或 pandas 读取此 CSV 文件进行查看和分析。
