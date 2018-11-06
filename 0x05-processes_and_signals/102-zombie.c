#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/**
 * main - creates 5 zombies children
 * Return: Always 0
 */
int main(void)
{
	pid_t c_pid;
	int count;

	while (count < 5)
	{
		c_pid = fork();
		if (c_pid)
			printf("Zombie process created, PID: %d\n", c_pid);
		else
			exit(0);
		count++;
	}
	sleep(100);

	return (0);
}
