# -*- coding: utf-8 -*-
import requests
import re

# === 用户输入区 ===
api_key = "不给你看"
user_id = "lockon"
base_url = "https://milesight-demo-use-only.eu1.cloud.thethings.industries"  # 创建网关用

# === 网关信息 ===
gateway_id = "24E124FFFE000003"
gateway_eui = "24E124FFFE000003"
gateway_name = "Auto-Gateway_" + gateway_id
gateway_description = "This is a test gateway created by autobot."
frequency_plan_id = "US_902_928_FSB_2"  # 这里是 EU 863-870 的频率计划 ID

# === gateway_id 清洗 ===
gateway_id = re.sub(r'[^a-zA-Z0-9-]', '-', gateway_id).lower()
if len(gateway_id) < 3:
    raise ValueError("gateway_id 长度必须 ≥ 3")

# === 构建请求数据 ===
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "gateway": {
        "ids": {
            "gateway_id": gateway_id,
            "eui": gateway_eui
        },
        "name": gateway_name,
        "frequency_plan_ids": [frequency_plan_id],
        "gateway_server_address": base_url.replace("https://", ""),
        "description": gateway_description,
        "location": {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "altitude": 0
        }
    }
}

# === 发送创建网关请求 ===
url = f"{base_url}/api/v3/users/{user_id}/gateways"
response = requests.post(url, json=data, headers=headers)

# === 输出结果 ===
if response.status_code in [200, 201]:
    print("✅ Gateway 创建成功！")
    print(response.json())

    # === 根据 frequency_plan_id 输出正确的 Semtech 地址 ===
    frequency_lns_map = {
        "EU_863_870": "eu1",
        "US_902_928": "nam1",  # 对应 US915
        "US_902_928_FSB_2": "nam1",  # 对应 US915
        "AU_915_928": "au1",
        "AS_923": "as1",
        "AS_923_1": "as1",
        "CN_470_510": "cn1",
        "IN_865_867": "in1",
        "KR_920_923": "kr1",
        "RU_864_870": "eu1",
        "RS_865_867": "eu1"
    }

    # 自动匹配区域前缀
    lns_region = frequency_lns_map.get(frequency_plan_id, "eu1")  # 默认 fallback 为 "eu1"
    
    semtech_address = f"{base_url.replace('https://', '')}:1700"
    print(f"\n🌐 Semtech 地址是：{semtech_address}")

else:
    print("❌ 创建失败，状态码：", response.status_code)
    print(response.text)
