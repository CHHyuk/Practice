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
	using Hybrid::HybFunc; //using을 이용해 '이름공간 Hybrid에 정의된 HybFunc를 호출할 때는 이름공간을 지정하지 않고 호출하겠다'는 것을 선언함
	HybFunc();  // 14행의 using선언을 통해 이름공간의 지정없이 HybFunc 함수를 호출하고 있음
	return 0;
}
