**Sản phẩm nộp**: 
+ Báo cáo bằng Word + Code+ Clip.
+ Báo cáo bằng word có từ 5-10 trang. 
+ Trang bìa làm bằng Canva report template, bên trong sơ đồ vẽ bằng Figma. Clip quay demo chương trình sinh viên chạy.

---
**Đề tài 7. Danh sách liên kết và quản lý bộ nhớ trong C.**
(Linked Lsit and Memory management in C)
> Remember, understanding pointers and memory allocation is crucial in C. T

```c
@parem // parameter
```
Quản lý bộ nhớ: cung cấp đủ bộ nhớ và dọn bộ nhớ sau khi sử dụng.

Code documentation
```c
struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
```
+ `struct Node* newNode`: This declares a pointer variable named `newNode` of type `struct Node*`, which means it is a pointer to a structure of type `Node`. This structure likely represents a node in a linked list.

+ `malloc(sizeof(struct Node))`: This is a function call to `malloc`, which stands for "memory allocation". It dynamically allocates memory on the heap for the size of the structure `Node`. The `sizeof` operator is used to determine the size of the structure in bytes.

+ `(struct Node*)`: The return value of `malloc` is a void pointer (`void*`), so it needs to be cast to the appropriate pointer type, which is `struct Node*` in this case. This allows the allocated memory to be treated as a `Node` structure.

```c
#include <stdio.h>   // Standard Input/Output library
#include <stdlib.h>  // Standard Library for general functions


//! 1. Define node Structure
struct Node {
    int data;          // Data to be stored in the node
    struct Node* next; // Pointer to the next node
};

//! 2. Create Head Pointer
struct Node* head = NULL;

//! 3. Create Nodes and Link Them
void createAndLinkNodes(int v) {
    // Create a new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

    // Assign data to the node
    newNode->data = v;  // Example data

    // Link the new node to the existing list
    newNode->next = head;

    // Update the head pointer to point to the new node
    head = newNode;
}

//! 4. Traverse (Duyệt) the List :
void traverseList() {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
}

//! 5. Insert Nodes
// Insert at the beginning
void insertAtBeginning(int data) {
    
    // Allocate memory for a new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data; // Assign the given data to the new node
    newNode->next = head;
    head = newNode;
}

// Insert at the end
void insertAtEnd(int data) {
    // Allocate memory for a new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data; // Assign the given data to the new node
    newNode->next = NULL;

    // assigned head to the node if the list is empty
    if (head == NULL) {
        head = newNode;
        return;
    }

    
    // Traverse to the end of the list
    struct Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    // Link the new node to the end of the list
    current->next = newNode;
}

//! 6. Delete Nodes
// Delete a node with a specific value
void deleteNode(int data) {
    struct Node* temp = head;
    struct Node* prev = NULL;

    if (temp != NULL && temp->data == data) {
        head = temp->next;
        free(temp);
        return;
    }

    while (temp != NULL && temp->data != data) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        return;
    }

    prev->next = temp->next;
    free(temp);
}

// Hàm giải phóng bộ nhớ của danh sách liên kết
// Free the memory of the linked list
void freeLinkedList() {
    struct Node* current = head;
    struct Node* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }

    head = NULL; // Reset the head pointer
}


int main() {
    createAndLinkNodes(5); // Create and link nodes
    createAndLinkNodes(10); // Create and link nodes
    createAndLinkNodes(11); // Create and link nodes
    createAndLinkNodes(7); // Create and link nodes
    createAndLinkNodes(2); // Create and link nodes
    insertAtEnd(211); // Insert at the end
    
    traverseList(); // Traverse the list and print the data
    
    freeLinkedList(); // Free the memory of the linked list
    printf("\n Linked list after free up memory");
    traverseList(); // Traverse the list and print the data
    
    return 0;
}

```