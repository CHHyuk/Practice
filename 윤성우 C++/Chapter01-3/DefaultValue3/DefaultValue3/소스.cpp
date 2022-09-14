#include<iostream>
int Boxvolume(int length, int width = 1, int height = 1);  // length 변수에 디폴트값이 없으므로 Boxvolume 함수를 호출할 때 반드시 하나 이상의 인자를 전달하여아 함

int main(void)
{
	std::cout << "[3, 3, 3] : " << Boxvolume(3, 3, 3) << std::endl; 
	std::cout << "[5, 5, D] : " << Boxvolume(5, 5) << std::endl;
	std::cout << "[7, D, D] : " << Boxvolume(7) << std::endl;
//	std::cout << "[D, D, D] : " << Boxvolume( ) << std::endl; // length 변수에 디폴트값이 지정되지 않았으므로 컴파일 에러
	return 0;
}

int Boxvolume(int length, int width, int height)
{
	return length * width * height;  // Boxvolume 함수는 length x width x height 라고 정함
}