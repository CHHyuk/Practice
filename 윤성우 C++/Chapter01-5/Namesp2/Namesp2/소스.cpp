#include<iostream>

namespace BestComImpl
{
	void SimpleFunc(void);     // BestComImpl�̶�� �̸����� �ȿ� �Լ��� ���� ����
}                           

namespace ProgComImpl
{
	void SimpleFunc(void);     // ProgComImpl�̶�� �̸����� �ȿ� �Լ��� ���� ����
}

int main(void)
{
	BestComImpl::SimpleFunc();
	ProgComImpl::SimpleFunc();
	return 0;
}

void BestComImpl::SimpleFunc(void)  // simplefunc�� ���ǵ� �κ�, �ش� ������ ��µǴ� �Լ�
{
	std::cout << "BestCom�� ������ �Լ�" << std::endl;
}

void ProgComImpl::SimpleFunc(void)  // simplefunc�� ���ǵ� �κ�, �ش� ������ ��µǴ� �Լ�
{
	std::cout << "ProgCom�� ������ �Լ�" << std::endl;
}