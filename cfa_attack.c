#include <stdio.h>

void funcA() {
    printf("Executing Function A\n");
}

void funcB() {
    printf("Executing Function B\n");
}

void funcC() {
    printf("Executing Function C\n");
}

int main() {
    printf("Starting Control Flow Simulation\n");
    funcA();
    funcB();
    funcC();
    printf("Ending Control Flow Simulation\n");
    return 0;
}
