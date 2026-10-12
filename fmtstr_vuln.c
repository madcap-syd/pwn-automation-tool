#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int target = 0x00000000;

void win() {
    printf("Congratulations! You won!\n");
    system("/bin/sh");
}

void vuln() {
    char buf[128];
    printf("Enter your message: ");
    fflush(stdout);
    
    fgets(buf, sizeof(buf), stdin);
    
    // УЯЗВИМОСТЬ: пользовательский ввод напрямую в printf!
    printf(buf); 
    
    printf("\nTarget value is: 0x%08x\n", target);
    
    if (target == 0xDEADBEEF) {
        win();
    } else {
        printf("Target is not 0xDEADBEEF. Try harder!\n");
    }
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("=== Format String Challenge ===\n");
    printf("Target address: %p\n", &target);
    vuln();
    return 0;
}
