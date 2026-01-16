#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
    int capacity;
} CustomList;

void init(CustomList *l) {
    l->size = 0;
    l->capacity = 2;
    l->data = malloc(l->capacity * sizeof(int));
}

void resize(CustomList *l) {
    l->capacity *= 2;
    l->data = realloc(l->data, l->capacity * sizeof(int));
}

// Python: list.append(x)
void append(CustomList *l, int x) {
    if (l->size == l->capacity) resize(l);
    l->data[l->size++] = x;
}

// Python: list.insert(i, x)
void insert(CustomList *l, int index, int x) {
    if (index < 0 || index > l->size) return;
    if (l->size == l->capacity) resize(l);
    for (int i = l->size; i > index; i--) l->data[i] = l->data[i-1];
    l->data[index] = x;
    l->size++;
}

// Python: list.pop([i])
int pop(CustomList *l, int index) {
    if (index < 0 || index >= l->size) return -1;
    int val = l->data[index];
    for (int i = index; i < l->size - 1; i++) l->data[i] = l->data[i+1];
    l->size--;
    return val;
}

// Python: list.remove(x)
void remove_val(CustomList *l, int x) {
    for (int i = 0; i < l->size; i++) {
        if (l->data[i] == x) {
            pop(l, i);
            return;
        }
    }
}

// Python: list.index(x)
int index_of(CustomList *l, int x) {
    for (int i = 0; i < l->size; i++) if (l->data[i] == x) return i;
    return -1;
}

void print_list(CustomList *l) {
    printf("[");
    for (int i = 0; i < l->size; i++) printf("%d%s", l->data[i], i == l->size - 1 ? "" : ", ");
    printf("]\n");
}

int main() {
    CustomList list;
    init(&list);
    append(&list, 10);
    append(&list, 20);
    insert(&list, 1, 15); // [10, 15, 20]
    print_list(&list);
    pop(&list, 2);        // [10, 15]
    print_list(&list);
    free(list.data);
    return 0;
}