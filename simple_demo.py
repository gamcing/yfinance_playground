# 用python输出电脑的mac地址、当前的ip内网地址、公网ip地址(cip.cc)
import uuid
import socket

def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

def get_local_ip_address():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip_address():
    import requests
    try:
        response = requests.get('https://cip.cc')
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "无法获取公网IP地址"
    except Exception as e:
        return f"获取公网IP地址时发生错误: {e}"

if __name__ == "__main__":
    # 先读取用户的输入
    user_name = input("请输入你的名字：")
    # 再拼接字符串
    result_str = f"""你好，{user_name}！以下是你的电脑信息：\n
    MAC地址: {get_mac_address()}\n
    内网IP地址: {get_local_ip_address()}\n
    公网IP地址: {get_public_ip_address()}"""
    print(result_str)
    
