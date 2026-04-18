#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
int main() {
    pid_t pid = fork();
    if (pid < 0) { perror("fork"); exit(1); }
    if (pid == 0) {
        printf("Child (PID %d): Exiting now.\n", getpid());
        exit(0);
    }
    printf("Parent: Child PID %d. Sleeping 10s before calling wait()...\n", pid);
    sleep(10);
    int status;
    wait(&status);
    printf("Parent: Called wait(). Zombie is gone.\n");
    sleep(10);
    return 0;
}
