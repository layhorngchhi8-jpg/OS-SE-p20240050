#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <pthread.h>

volatile int keep_running = 1;

void sig_handler(int signo) {
    if (signo == SIGINT) {
        printf("\n[Signal Caught] SIGINT received. Signaling threads to stop...\n");
        keep_running = 0;
    }
}

void* worker_func(void* arg) {
    long tid = (long)arg;
    printf("Worker thread %ld started.\n", tid);
    while (keep_running) {
        printf("Thread %ld is working...\n", tid);
        sleep(1);
    }
    printf("Worker thread %ld exiting cleanly.\n", tid);
    pthread_exit(NULL);
}

int main() {
    signal(SIGINT, sig_handler);

    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, worker_func, (void*)1L);
    pthread_create(&thread2, NULL, worker_func, (void*)2L);

    printf("Main: Two worker threads spawned. Press Ctrl+C to shut down.\n");

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("All threads cleanly exited. Goodbye.\n");
    return 0;
}
