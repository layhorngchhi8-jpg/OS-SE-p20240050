#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

void handler(int sig)
{
    if (sig == SIGINT)
        printf("\nCaught SIGINT (Ctrl+C). Cleaning up...\n");

    if (sig == SIGTERM)
        printf("\nCaught SIGTERM. Cleaning up...\n");

    exit(0);
}

int main()
{
    signal(SIGINT, handler);
    signal(SIGTERM, handler);

    printf("Program running... PID = %d\n", getpid());

    while (1)
    {
        printf("Working...\n");
        sleep(2);
    }

    return 0;
}
