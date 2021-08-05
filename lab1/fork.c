#include<stdio.h>
#include<unistd.h>

int main(){
    pid_t ret_value;
    printf("\n The process id is %d\n", getpid());
    
    ret_value = fork();
    if(ret_value<0){
        //fork has failed
        printf("\n Child Process\n");
        printf("The process id is %d\n ", getpid());
        sleep(20);
    }
    else if(ret_value==0){
        printf("\n Child Process \n");
        printf("The process id is %d \n", getpid());
        sleep(30);
    }
    else{
        //parent process
        wait();
        printf("Parent Process\n");
        printf("The process id is %d\n", getpid());
        sleep(30);
    }
    return 0;
}