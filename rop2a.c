#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

void rop1() {
    printf("ROP 1!\n");
}

void rop2() {
    printf("ROP 2!\n");
}

void rop3() {
    printf("ROP 3!\n");
    
    // Execute the Python DDoS simulation script
    system("python3 /home/pi/ddos_attack_simulation.py &");
}

void vulnerable(char* string) {
    char buffer[100];
    strcpy(buffer, string);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;  // Exit with error if no input is provided
    }
    vulnerable(argv[1]);
    
    // Keep the process running
    while (1) {
        sleep(1);
    }

    return 0;
}