#include <cow/optional.h>
#include <iostream>
#include <string>

int main() {
	cow::optional<std::string> str{"Test application successfully ran\n"};
	std::cout << *str;
}
