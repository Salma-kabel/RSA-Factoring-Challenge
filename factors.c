#define  _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main(int argc, char **argv)
{
	char *line;
	size_t len = 1024;
	int m = 0;
	FILE *file;
	if (argc != 2)
		return (1);

	file = fopen(argv[1], "r");
	if (file == NULL)
		return (1);
	while (getline(&line, &len, file) != -1)
	{
		printf("%s\n", line);
		printf("%d\n", m);
		/*num = atoi(line);
		printf("%ld\n", num);*/
	}
	return (1);
}
