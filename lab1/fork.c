#include<stdio.h>
#include<unistd.h>

int main(){
    pid_t process_id;
    printf("\n The process id is %d\n", getpid());
    
    process_id = fork();
    if(process_id<0){
        //fork has failed
        printf("\n Child Process\n");
        printf("The process id is %d\n ", getpid());
    }
    else if(process_id==0){
        printf("\n Child Process \n");
        printf("The process id is %d \n", getpid());
        sleep(10);
    }
    else{
        //parent process
        wait();
        printf("Parent Process\n");
        printf("The process id is %d\n", getpid());
        sleep(20);
    }
    return 0;
}