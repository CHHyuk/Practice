#include <iostream>

namespace BestComImpl // BestComImpl 이라는 이름의 공간을 마련하여 그 안에 SimpleFunc를 정의하였음, 따라서 이 함수는 'BestComImpl::SimpleFunc()' 이라고 지칭됨
{
	void SimpleFunc(void)
	{
		std::cout << "BestCom이 정의한 함수" << std::endl;
	}
}

namespace ProgComImpl // ProgComImpl 이라는 이름의 공간을 마련하여 그 안에 SimpleFunc를 정의하였음, 따라서 이 함수는 'ProgComImpl::SimpleFunc()' 이라고 지칭됨
{
	void SimpleFunc(void)
	{
		std::cout << "ProgCom이 정의한 함수" << std::endl;
	}
}

int main(void)
{
	BestComImpl::SimpleFunc(); // 이름공간 BestComImpl 내에 정의된 함수 SimpleFunc의 호출문장
	ProgComImpl::SimpleFunc(); // 이름공간 ProgComImpl 내에 정의된 함수 SimpleFunc의 호출문장
	return 0;
}