# FinDoc Stock API · 金融股票数据查询接口

一个基于 FastAPI 的轻量级金融数据查询服务，输入股票代码即可返回该股票近一个月的涨跌情况。本项目是「金融文档智能助手（FinDocAssistant）」系列的第一步，专注于数据获取与接口化。

## ✨ 功能特性

- 查询任意股票代码近一个月的价格涨跌情况
- 返回期初/期末收盘价、涨跌额、涨跌幅（百分比）
- 数据实时来源于雅虎财经（通过 yfinance）
- 自带交互式接口文档（FastAPI 自动生成）

## 🛠️ 技术栈

- **Python 3.10**
- **FastAPI** —— Web 接口框架
- **Uvicorn** —— ASGI 服务器
- **yfinance** —— 金融数据获取
- **pandas** —— 数据处理

## 🚀 如何运行

1. 克隆本仓库并进入项目目录：
   ```bash
   git clone 【你的仓库地址】
   cd findoc-01-api
   ```

2. 创建并激活虚拟环境：
   ```bash
   python -m venv venv
   # Windows (Git Bash)
   source venv/Scripts/activate
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 启动服务：
   ```bash
   uvicorn api:app --reload
   ```

5. 打开浏览器访问 `http://127.0.0.1:8000/docs` 查看交互式接口文档。

## 📡 接口说明

### 查询股票涨跌情况

```
GET /stock/{symbol}
```

**路径参数：**

| 参数 | 类型 | 说明 | 示例 |
|------|------|------|------|
| symbol | string | 股票代码 | AAPL |

**请求示例：**

```
GET http://127.0.0.1:8000/stock/AAPL
```

**返回示例：**

```json
{
  "symbol": "AAPL",
  "first_close": 308.33,
  "last_close": 297.01,
  "change": -11.32,
  "change_percent": -3.67
}
```

## 📁 项目结构

```
findoc-01-api/
├── api.py              # FastAPI 应用与接口定义
├── stock.py            # 股票数据获取与计算逻辑
├── requirements.txt    # 项目依赖清单
├── .gitignore          # Git 忽略配置
└── README.md           # 项目说明
```

## 🗺️ 后续计划

本项目是 FinDocAssistant 系列的起点，后续将逐步演进为：

- 接入大语言模型，实现自然语言查询财报数据（Agent）
- 构建可溯源的金融文档 RAG 问答系统
- 生产级部署、监控与成本优化

---

*本项目用于学习 AI 应用工程，欢迎交流。*
