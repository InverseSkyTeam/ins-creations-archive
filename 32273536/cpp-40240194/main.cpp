#include <iostream>
#include <string>
#include <stdarg.h>



int m_printf(const char* format,...) 
{
	std::string data = format;
	std::string result = "";
	int count = 0;
	va_list v_args;
	va_start(v_args, format);
	for (int i = 0; i < data.length(); i++)
	{
		char current_char = data[i];
		switch (current_char)
		{
		case '%':
		{
			if (data.length() - 1 - 1 >= i)
			{
				char current_char_next = data[i + 1];
				switch (current_char_next)
				{
				case '%':
				{
					result += '%';
					break;
				}
				case 'd':
				{
					int number = va_arg(v_args, int);
					result += std::to_string(number);
					break;
				}
				case 's':
				{
					const char* content = va_arg(v_args, const char*);
					result += content;
					break;
				}
				case 'c':
				{
					char text = va_arg(v_args, char);
					result += text;
					break;
				}
				default:
				{
					result += '%' + current_char_next;
					break;
				}
				}
				i++;
				break;
			}
			else
			{
				break;
			}
		}
		default:
		{
			result += current_char;
			break;
		}
		}
	}
	std::cout << result;
	va_end(v_args);
	return count;
}
int main(int argv,char* args[]) 
{
	std::string output = "今天读《C++ Primer》注意到了变参函数,于是百度有关教程，仿写了一个printf()函数。当然，功能极其简陋，但足以打印这条信息。注意，变参函数是C样式.";
	m_printf("%s\n",output.c_str());
}