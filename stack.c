#include <stdio.h>
#include <stdbool.h>
#include <limits.h>  
#define MAX_SIZE 100  


typedef struct {
    int data[MAX_SIZE];  
    int top;             
} Stack;


void stack_init(Stack *s) {
    s->top = -1;  
}


bool stack_is_empty(Stack *s) {
    return s->top == -1;
}


bool stack_is_full(Stack *s) {
    return s->top == MAX_SIZE - 1;
}


bool stack_push(Stack *s, int item) {
    if (stack_is_full(s)) {
        printf("Error: Stack overflow\n");
        return false;  
    }
    s->data[++(s->top)] = item; 
    return true; 
}


int stack_pop(Stack *s) {
    if (stack_is_empty(s)) {
        printf("Error: Stack underflow\n");
        return INT_MIN;  
    }
    return s->data[(s->top)--];  
}


int stack_peek(Stack *s) {
    if (stack_is_empty(s)) {
        printf("Error: Stack is empty\n");
        return INT_MIN; 
    }
    return s->data[s->top]; 
}


void stack_print(Stack *s) {
    if (stack_is_empty(s)) {
        printf("Stack is empty\n");
        return;
    }
    printf("Stack contents (top to bottom):\n");
    for (int i = s->top; i >= 0; i--) {
        printf("%d\n", s->data[i]);
    }
}


int main() {
    Stack s; 
    stack_init(&s);  

    
    printf("Pushing items onto the stack:\n");
    stack_push(&s, 10);
    stack_push(&s, 20);
    stack_push(&s, 30);

   
    stack_print(&s);

  
    int top_item = stack_peek(&s);
    printf("Top item is: %d\n", top_item);

  
    int popped_item = stack_pop(&s);
    printf("Popped item is: %d\n", popped_item);

  
    printf("Stack after popping one item:\n");
    stack_print(&s);

  
    stack_pop(&s);
    stack_pop(&s);
    stack_pop(&s);  
    return 0;
}
