class CustomList {
    constructor() {
        this.capacity = 2;
        this.size = 0;
        this.data = new Array(this.capacity);
    }

    append(value) {
        if (this.size === this.capacity) this._resize();
        this.data[this.size++] = value;
    }

    insert(index, value) {
        if (index < 0 || index > this.size) return;
        if (this.size === this.capacity) this._resize();
        for (let i = this.size; i > index; i--) {
            this.data[i] = this.data[i - 1];
        }
        this.data[index] = value;
        this.size++;
    }

    _resize() {
        this.capacity *= 2;
        let newData = new Array(this.capacity);
        for (let i = 0; i < this.size; i++) newData[i] = this.data[i];
        this.data = newData;
    }

    pop() {
        if (this.size === 0) return null;
        return this.data[--this.size];
    }

    display() {
        let result = [];
        for(let i=0; i<this.size; i++) result.push(this.data[i]);
        console.log("[" + result.join(", ") + "]");
    }
}

const list = new CustomList();
list.append("Python");
list.append("Rules");
list.insert(1, "Always");
list.display(); // [Python, Always, Rules]