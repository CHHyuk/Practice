#include <iostream>

namespace BestComImpl   // BestComImpl �̶�� �̸������� �� �������� �������� ���� �Ǿ����� ���� �������� ���ֵ�
{
	void SimpleFunc(void);
}

namespace BestComImpl   // BestComImpl �̶�� �̸������� �� �������� �������� ���� �Ǿ����� ���� �������� ���ֵ�
{
	void PrettyFunc(void);
}

namespace ProgComImpl
{
	void SimpleFunc(void);
}

int main(void)
{
	BestComImpl::SimpleFunc();
	return 0;
}

void BestComImpl::SimpleFunc(void)
{
	std::cout << "BestCom�� ������ �Լ�" << std::endl;
	PrettyFunc();  // ���� BestComImpl�̶�� �̸������� ���ǵ� �Լ��̹Ƿ� �̷��� ����ȣ���� ������
	ProgComImpl::SimpleFunc();  // ProgComImpl�� ���ǵ� �Լ� SimpleFunc�� ȣ���ϴ� ����� ȣ�� ��ġ�� ���� ���� ����
}

void BestComImpl::PrettyFunc(void)
{
	std::cout << "So Pretty!!" << std::endl;  // PrettyFunc�� �Լ� ����
}

void ProgComImpl::SimpleFunc(void)
{
	std::cout << "ProgCom�� ������ �Լ�" << std::endl;  // SimpleFunc(ProgComImpl)�� �Լ� ����
}
