#include <iostream>

namespace BestComImpl // BestComImpl �̶�� �̸��� ������ �����Ͽ� �� �ȿ� SimpleFunc�� �����Ͽ���, ���� �� �Լ��� 'BestComImpl::SimpleFunc()' �̶�� ��Ī��
{
	void SimpleFunc(void)
	{
		std::cout << "BestCom�� ������ �Լ�" << std::endl;
	}
}

namespace ProgComImpl // ProgComImpl �̶�� �̸��� ������ �����Ͽ� �� �ȿ� SimpleFunc�� �����Ͽ���, ���� �� �Լ��� 'ProgComImpl::SimpleFunc()' �̶�� ��Ī��
{
	void SimpleFunc(void)
	{
		std::cout << "ProgCom�� ������ �Լ�" << std::endl;
	}
}

int main(void)
{
	BestComImpl::SimpleFunc(); // �̸����� BestComImpl ���� ���ǵ� �Լ� SimpleFunc�� ȣ�⹮��
	ProgComImpl::SimpleFunc(); // �̸����� ProgComImpl ���� ���ǵ� �Լ� SimpleFunc�� ȣ�⹮��
	return 0;
}