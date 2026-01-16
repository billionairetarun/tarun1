import java.util.Arrays;

public class CustomList {
    private int[] data;
    private int size;

    public CustomList() {
        data = new int[2];
        size = 0;
    }

    public void append(int value) {
        ensureCapacity();
        data[size++] = value;
    }

    public void insert(int index, int value) {
        if (index < 0 || index > size) throw new IndexOutOfBoundsException();
        ensureCapacity();
        for (int i = size; i > index; i--) data[i] = data[i-1];
        data[index] = value;
        size++;
    }

    private void ensureCapacity() {
        if (size == data.length) {
            data = Arrays.copyOf(data, data.length * 2);
        }
    }

    public int pop() {
        if (size == 0) throw new RuntimeException("Empty list");
        return data[--size];
    }

    @Override
    public String toString() {
        int[] activePart = Arrays.copyOfRange(data, 0, size);
        return Arrays.toString(activePart);
    }

    public static void main(String[] args) {
        CustomList list = new CustomList();
        list.append(10);
        list.append(30);
        list.insert(1, 20);
        System.out.println(list); // [10, 20, 30]
    }
}