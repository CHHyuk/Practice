#include<iostream>
int Boxvolume(int length, int width = 1, int height = 1);  // length ������ ����Ʈ���� �����Ƿ� Boxvolume �Լ��� ȣ���� �� �ݵ�� �ϳ� �̻��� ���ڸ� �����Ͽ��� ��

int main(void)
{
	std::cout << "[3, 3, 3] : " << Boxvolume(3, 3, 3) << std::endl; 
	std::cout << "[5, 5, D] : " << Boxvolume(5, 5) << std::endl;
	std::cout << "[7, D, D] : " << Boxvolume(7) << std::endl;
//	std::cout << "[D, D, D] : " << Boxvolume( ) << std::endl; // length ������ ����Ʈ���� �������� �ʾ����Ƿ� ������ ����
	return 0;
}

int Boxvolume(int length, int width, int height)
{
	return length * width * height;  // Boxvolume �Լ��� length x width x height ��� ����
}