#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

#define MAX_SIZE 100


typedef struct {
    int data[MAX_SIZE];  
    int front;           
    int rear;            
    int size;            
} Queue;


void queue_init(Queue *q) {
    q->front = 0;
    q->rear = -1;
    q->size = 0;
}


bool queue_is_empty(Queue *q) {
    return q->size == 0;
}


bool queue_is_full(Queue *q) {
    return q->size == MAX_SIZE;
}


void queue_enqueue(Queue *q, int item) {
    if (queue_is_full(q)) {
        printf("Error: Queue overflow\n");
        return;
    }
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = item;
    q->size++;
}


int queue_dequeue(Queue *q) {
    if (queue_is_empty(q)) {
        printf("Error: Queue underflow\n");
        return INT_MIN;  
    }
    int item = q->data[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    q->size--;
    return item;
}


int queue_front(Queue *q) {
    if (queue_is_empty(q)) {
        printf("Error: Queue is empty\n");
        return INT_MIN;  
    }
    return q->data[q->front];
}


void queue_print(Queue *q) {
    if (queue_is_empty(q)) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue contents (front to rear):\n");
    int count = q->size;
    int index = q->front;
    while (count > 0) {
        printf("%d ", q->data[index]);
        index = (index + 1) % MAX_SIZE;
        count--;
    }
    printf("\n");
}


int main() {
    Queue q;  
    queue_init(&q);  


    printf("Enqueuing items:\n");
    queue_enqueue(&q, 10);
    queue_enqueue(&q, 20);
    queue_enqueue(&q, 30);


    queue_print(&q);


    int front_item = queue_front(&q);
    printf("Front item: %d\n", front_item);


    int dequeued_item = queue_dequeue(&q);
    printf("Dequeued item: %d\n", dequeued_item);

 
    printf("Queue after dequeuing one item:\n");
    queue_print(&q);

    
    queue_dequeue(&q);
    queue_dequeue(&q);
    queue_dequeue(&q);  

    return 0;
}
