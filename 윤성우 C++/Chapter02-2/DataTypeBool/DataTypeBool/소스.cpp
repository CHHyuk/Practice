#include <iostream>
using namespace std;

bool IsPositive(int num) // bool�� �⺻ �ڷ����̱� ������ �Լ��� ��ȯ�����ε� ������ ����
{
	if (num <= 0)
		return false;
	else
		return true;
}

int main(void)
{
	bool isPos; // bool�� ������ ������ �Լ� IsPositive�� ��ȯ�ϴ� bool�� �����͸� �����ϰ� ����
	int num;
	cout << "Input number: ";
	cin >> num;

	isPos = IsPositive(num); // bool�� ������ ������ �Լ� IsPositive�� ��ȯ�ϴ� bool�� �����͸� �����ϰ� ����
	if (isPos)
		cout << "Positive number" << endl;
	else
		cout << "Negative number" << endl;
	return 0;
}