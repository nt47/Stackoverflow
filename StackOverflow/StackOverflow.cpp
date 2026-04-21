#include <cstdio>
#include <cstdlib>
#include <Windows.h>


const WCHAR* text = L"Hijack成功！";

void Hijack(HWND hwnd, LPCWSTR lpText, LPCWSTR lpCaption, UINT uType) {
	MessageBoxW(hwnd, lpText, lpCaption, uType);
	exit(0);//栈被觉得稀巴烂，没法恢复了，直接退出
}

void secret_function() {
	printf("\n[SUCCESS] 控制流劫持成功！正在启动 Shell...\n");
	system("cmd.exe");
	exit(0);
}

__declspec(noinline)
void vulnerable() {
	char buffer[16]; // 16 字节的小池塘
	printf("等待输入 (fread模式)... \n");

	// 关键点：fread 允许读取 \x00，且不检查边界
	fread(buffer, 1, 128, stdin);
}

int main() {
	printf("secret_function 地址: %p\n", &secret_function);
	printf("Hijack 地址: %p\n", &Hijack);
	printf("text 地址: %p\n", text);

	vulnerable();
	printf("正常退出。\n");
	return 0;
}