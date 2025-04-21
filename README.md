# TTN Gateway 创建工具

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)

通过 The Things Network (TTN) API 自动创建 LoRaWAN 网关的工具。

## 功能特性
- 通过 REST API 创建 TTN 网关
- 自动配置网关参数（ID、EUI、频率计划等）
- 自动计算 Semtech 数据包转发地址
- 错误处理和输入验证

## 快速开始
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 配置参数：
   修改 `ttn-gateway.py` 中的用户参数：
   ```python
   api_key = "YOUR_API_KEY"
   user_id = "YOUR_USER_ID"
   gateway_id = "YOUR_GATEWAY_ID"
   ```

3. 运行程序：
   ```bash
   python ttn-gateway.py
   ```
