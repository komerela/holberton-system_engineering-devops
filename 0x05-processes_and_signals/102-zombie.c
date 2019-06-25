#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Runs a test for infinite loop
 *
 *
 * Return: 0 for success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Main for zombie program
 *
 *
 * Return: 0 for success
 */

int main(void)
{
	int i;
	int pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == -1)
			continue;
		else if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: ZOMBIE_PID: %d\n", pid);
	}
	infinite_while();
	return (0);
}
