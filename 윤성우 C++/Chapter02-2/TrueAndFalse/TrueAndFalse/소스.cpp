#include<iostream>
using namespace std;

int main(void)
{
	int num = 10;
	int i = 0;

	cout << "true: " << true << endl;
	cout << "false: " << false << endl;  // true = 1 false = 0 ���� ���

	while (true)  // ���ѷ��� ������ ���� ���� ���� 1�� ��������� �̷��� true�� ����� ���� �ִ�.
	{
		cout << i++ << ' ';
		if (i > num)
			break;
	}
	cout << endl;

	cout << "sizeof 1: " << sizeof(1) << endl; 
	cout << "sizeof 0: " << sizeof(0) << endl; // 1�� 0�� �޸𸮰����� Ȯ���ϴ� ����
	cout << "sizeof true: " << sizeof(true) << endl;
	cout << "sizeof false: " << sizeof(false) << endl; // true�� false�� �޸𸮰����� Ȯ���ϴ� ����
	return 0;
}