#include <iostream>
#include <stdexcept>

class CustomList {
private:
    int* data;
    int _size;
    int _capacity;

    void resize() {
        _capacity *= 2;
        int* newData = new int[_capacity];
        for (int i = 0; i < _size; i++) newData[i] = data[i];
        delete[] data;
        data = newData;
    }

public:
    CustomList() : _size(0), _capacity(2) {
        data = new int[_capacity];
    }

    void append(int value) {
        if (_size == _capacity) resize();
        data[_size++] = value;
    }

    void insert(int index, int value) {
        if (index < 0 || index > _size) throw std::out_of_range("Index out of bounds");
        if (_size == _capacity) resize();
        for (int i = _size; i > index; i--) data[i] = data[i - 1];
        data[index] = value;
        _size++;
    }

    int pop() {
        if (_size == 0) throw std::underflow_error("List is empty");
        return data[--_size];
    }

    void display() {
        std::cout << "[";
        for (int i = 0; i < _size; i++) 
            std::cout << data[i] << (i == _size - 1 ? "" : ", ");
        std::cout << "]" << std::endl;
    }

    ~CustomList() { delete[] data; }
};

int main() {
    CustomList list;
    list.append(5);
    list.append(15);
    list.insert(0, 1); // [1, 5, 15]
    list.display();
    return 0;
}