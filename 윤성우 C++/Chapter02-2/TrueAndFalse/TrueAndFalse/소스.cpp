#include<iostream>
using namespace std;

int main(void)
{
	int num = 10;
	int i = 0;

	cout << "true: " << true << endl;
	cout << "false: " << false << endl;  // true = 1 false = 0 임을 출력

	while (true)  // 무한루프 형성을 위해 보통 숫자 1을 사용하지만 이렇게 true를 사용할 수도 있다.
	{
		cout << i++ << ' ';
		if (i > num)
			break;
	}
	cout << endl;

	cout << "sizeof 1: " << sizeof(1) << endl; 
	cout << "sizeof 0: " << sizeof(0) << endl; // 1과 0의 메모리공간을 확인하는 문장
	cout << "sizeof true: " << sizeof(true) << endl;
	cout << "sizeof false: " << sizeof(false) << endl; // true와 false의 메모리공간을 확인하는 문장
	return 0;
}