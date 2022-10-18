#include <iostream>

namespace BestComImpl   // BestComImpl 이라는 이름공간이 두 영역으로 나누어져 선언 되었지만 동일 공간으로 간주됨
{
	void SimpleFunc(void);
}

namespace BestComImpl   // BestComImpl 이라는 이름공간이 두 영역으로 나누어져 선언 되었지만 동일 공간으로 간주됨
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
	std::cout << "BestCom이 정의한 함수" << std::endl;
	PrettyFunc();  // 같은 BestComImpl이라는 이름공간에 정의된 함수이므로 이렇게 직접호출이 가능함
	ProgComImpl::SimpleFunc();  // ProgComImpl에 정의된 함수 SimpleFunc를 호출하는 방법은 호출 위치에 관계 없이 같다
}

void BestComImpl::PrettyFunc(void)
{
	std::cout << "So Pretty!!" << std::endl;  // PrettyFunc의 함수 선언
}

void ProgComImpl::SimpleFunc(void)
{
	std::cout << "ProgCom이 정의한 함수" << std::endl;  // SimpleFunc(ProgComImpl)의 함수 선언
}
