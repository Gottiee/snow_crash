#include <unistd.h>

int main(int argc, char **argv)
{
	if (argc != 2)
		return 1;
	char *exploit = argv[1];
	char c;
	for (int i = 0; exploit[i]; i++)
	{
		c = exploit[i] - i;
		write(1, &c, 1);
	}
	write(1, "\n", 1);
	return 0;
}