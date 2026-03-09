---
marp: true
title: Python导学
paginate: true
author: 金成
theme: default
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# Python: 安装与使用
金成，金融学院，金融科学实验中心
jincheng@sufe.edu.cn

---


## 本地安装Python：软件、环境
**切记：勾选上“ADD TO PATH”选项**
- Python官网：https://www.python.org/downloads/
- Anaconda/Miniconda： https://conda.io/
  - 国内(清华)：https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive
- 编程环境：
  - 记事本
  - Microsoft Visual Studio Code：https://code.visualstudio.com/
  - PyCharm：https://www.jetbrains.com/pycharm/
  - Jupyter Notebook / Jupyter Lab

---

## 软件包：pip、conda

### 安装插件通常在终端环境中进行
- cmd/PowerShell(Windows)、Terminal(macOS/Linux)
### pip：https://pypi.org
安装软件包的命令形如`pip install [package_name][==版本号(可不填)]`
例如，你想要安装tushare包，就是`pip install tushare`
### conda：预编译包
一些相对复杂的软件包，在pip中经常需要编译安装，不仅时间长而且可能会遇到各种问题，而conda提供了预编译包。
例如，用于做金融模拟、资产定价的QuantLib包，可以用`conda install -c conda-forge QuantLib-Python`安装

---
## 中国大陆用户的pip加速
由于pypi.org在国外，国内用户安装软件包时可能会很慢，可以使用国内的镜像源，此处我们推荐腾讯云：
- **临时使用**，在安装过程中指定镜像源：
```bash
pip install -i https://mirrors.tencent.com/pypi/simple tushare
```
- **永久使用**，用指令修改配置文件：
```bash
pip config set global.index-url https://mirrors.tencent.com/pypi/simple
pip config set trusted-host mirrors.tencent.com
pip config set trusted-host mirrors.cloud.tencent.com
```
---
## 云端编程
- GitHub Codespaces：https://github.com/codespaces/new
- Google Colab：https://colab.research.google.com/
- 腾讯云Cloud Studio
  - 类VS Code模式：https://ide.cloud.tencent.com/
  - 简易应用模式：https://cloudstudio.net/

---
## 运行第一个Python程序——完成第一阶段
- 使用终端试一试：
```cmd
python simple_demo.py
```
等同于以下“咒语”：
```cmd
python -c "print('hello maths master, 1+1=',1+1)"
```
- 使用编程环境试一试
  - Visual Studio Code
  - Jupyter Notebook
  - Cloud Studio

---
## 第二阶段：从金融Python教学项目学习pandas
- 先安装git: https://git-scm.com/install/
- 在VS Code中，拉取一个项目
```bash
git clone https://github.com/LastAncientOne/Stock_Analysis_For_Quant
```
*卡住了？*

可以尝试借助一些网游加速器加速GitHub：https://steampp.net/

---

## 第三阶段：使用tushare

- 官方文档：https://tushare.pro/document/2

```python
import tushare as ts
pro = ts.pro_api('你的tushare_token')
df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(df.head())
```
