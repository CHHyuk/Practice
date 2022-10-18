#include <iostream>

namespace Hybrid
{
	void HybFunc(void)
	{
		std::cout << "So simple function!" << std::endl;
		std::cout << "In namespace Hybrid!" << std::endl;
	}
}

int main(void)
{
	using Hybrid::HybFunc; //using�� �̿��� '�̸����� Hybrid�� ���ǵ� HybFunc�� ȣ���� ���� �̸������� �������� �ʰ� ȣ���ϰڴ�'�� ���� ������
	HybFunc();  // 14���� using������ ���� �̸������� �������� HybFunc �Լ��� ȣ���ϰ� ����
	return 0;
}
