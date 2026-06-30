#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_THREADS 3

void *worker(void *arg)
{
    int id = *(int *)arg;

    printf("Worker %d START (TID=%lu)\n", id, pthread_self());
    fflush(stdout);

    sleep(100);   // VERY IMPORTANT: keep thread alive long enough

    int *result = malloc(sizeof(int));
    *result = id * 100;

    printf("Worker %d END\n", id);

    pthread_exit(result);
}

int main()
{
    pthread_t threads[NUM_THREADS];
    int ids[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++)
    {
        ids[i] = i + 1;
        pthread_create(&threads[i], NULL, worker, &ids[i]);
    }

    int total = 0;

    for (int i = 0; i < NUM_THREADS; i++)
    {
        int *res;
        pthread_join(threads[i], (void**)&res);
        total += *res;
        free(res);
    }

    printf("Final Summary = %d\n", total);

    return 0;
}
