#include<iostream>

inline int SQUARE(int x) // �ζ��� �Լ��� ���� ��� ǥ��, SQUARE �Լ��� �ζ��� �Լ��� �Ǿ���
{
	return x * x; 
}

int main()
{
	std::cout << SQUARE(5) << std::endl; 
	std::cout << SQUARE(12) << std::endl; // SQUARE �Լ��� ȣ���ϰ�����, �׷��� �� �Լ��� �ζ��� �Լ��̴� ��ü�κ��� ȣ�⹮�� ��ü�ϰ� ��
	return 0;
}