#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 100

typedef struct {
    int data;
    int next;
} Node;

typedef struct {
    Node nodes[MAX_SIZE];
    int head;
    int free;
} LinkedList;

void list_init(LinkedList *list) {
    list->head = -1;
    list->free = 0;
    for (int i = 0; i < MAX_SIZE - 1; i++) {
        list->nodes[i].next = i + 1;
    }
    list->nodes[MAX_SIZE - 1].next = -1;
}

bool list_is_empty(LinkedList *list) {
    return list->head == -1;
}

bool list_is_full(LinkedList *list) {
    return list->free == -1;
}

int list_insert(LinkedList *list, int data) {
    if (list_is_full(list)) {
        printf("Error: List is full\n");
        return -1;
    }
    int new_node = list->free;
    list->free = list->nodes[new_node].next;
    list->nodes[new_node].data = data;
    list->nodes[new_node].next = list->head;
    list->head = new_node;
    return new_node;
}

bool list_remove(LinkedList *list, int data) {
    if (list_is_empty(list)) {
        return false;
    }
    int current = list->head;
    int prev = -1;
    while (current != -1 && list->nodes[current].data != data) {
        prev = current;
        current = list->nodes[current].next;
    }
    if (current == -1) {
        return false;
    }
    if (prev == -1) {
        list->head = list->nodes[current].next;
    } else {
        list->nodes[prev].next = list->nodes[current].next;
    }
    list->nodes[current].next = list->free;
    list->free = current;
    return true;
}

void list_print(LinkedList *list) {
    if (list_is_empty(list)) {
        printf("List is empty\n");
        return;
    }
    printf("List contents: ");
    int current = list->head;
    while (current != -1) {
        printf("%d ", list->nodes[current].data);
        current = list->nodes[current].next;
    }
    printf("\n");
}

int main() {
    LinkedList list;
    list_init(&list);

    printf("Inserting elements: 3, 7, 2, 5\n");
    list_insert(&list, 3);
    list_insert(&list, 7);
    list_insert(&list, 2);
    list_insert(&list, 5);

    list_print(&list);

    printf("Removing element: 7\n");
    if (list_remove(&list, 7)) {
        printf("7 removed successfully\n");
    } else {
        printf("7 not found in the list\n");
    }

    list_print(&list);

    printf("Inserting element: 9\n");
    list_insert(&list, 9);

    list_print(&list);

    printf("Trying to remove non-existent element: 10\n");
    if (list_remove(&list, 10)) {
        printf("10 removed successfully\n");
    } else {
        printf("10 not found in the list\n");
    }

    list_print(&list);

    return 0;
}
