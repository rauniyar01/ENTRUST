#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void vulnerable_function(char *input) {
    char buffer[64];
    strcpy(buffer, input);  // Unsafe copying with no bounds check
}

void secret_function() {
    printf("You have reached the secret function!\n");
    system("/bin/sh"); // Open a shell
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        vulnerable_function(argv[1]);
    } else {
        printf("Usage: %s <input>\n", argv[0]);
    }
    return 0;
}