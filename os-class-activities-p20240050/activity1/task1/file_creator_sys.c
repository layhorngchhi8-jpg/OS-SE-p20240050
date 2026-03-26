#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd;
    const char *text = "Hello from Operating Systems class!\n";
    const char *msg = "File created successfully!\n";

    fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

    if (fd < 0) {
        write(2, "Error opening file\n", 20);
        return 1;
    }

    write(fd, text, strlen(text));
    close(fd);

    write(1, msg, strlen(msg));

    return 0;
}
