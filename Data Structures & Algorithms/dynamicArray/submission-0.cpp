class DynamicArray {
private:
    int capacity;
    int *arr;
    int length;
public:

    DynamicArray(int capacity):length(0),capacity(capacity) {
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (length ==capacity){
            resize();}
        set(length, n);
        length++;      

    }

    int popback() {
        if (length)
            length--;
        return arr[length];
    }

    void resize() {
        capacity = 2 * capacity;
        int *newarray = new int[capacity];
        for (auto i = 0; i<length; i++){
            newarray[i] = arr[i];
        }
        arr = newarray;
    }

    int getSize() {
        return length;
    }

    int getCapacity(){
        return capacity;
    }
};
