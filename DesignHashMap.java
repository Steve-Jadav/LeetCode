# Problem 706

class Entry {
    private int key;
    private int value;
    
    public Entry(int key, int value) {
        this.key = key;
        this.value = value;
    }
    
    public int getKey() {
        return this.key;
    }
    
    public int getValue() {
        return this.value;
    }
    
    public void setValue(int value) {
        this.value = value;
    }
}

class MyHashMap {
    
    private static final int DEFAULT_SIZE = 10000;
    private static final double LOAD_FACTOR = 0.75;
    
    private int numberOfElements;
    private List<Entry>[] hashTable;
    
    /** Initialize your data structure here. */
    public MyHashMap() {
        this.hashTable = new List[DEFAULT_SIZE];
        this.numberOfElements = 0;
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        
        List<Entry> cell = getCell(key);
        
        for (Entry entry: cell) {
            if (entry.getKey() == key) {
                entry.setValue(value);
                return;
            }
        }
        this.numberOfElements ++;
        cell.add(new Entry(key, value));
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        List<Entry> cell = getCell(key);
        for (Entry entry: cell) {
            if (entry.getKey() == key)
                return entry.getValue();
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        List<Entry> cell = getCell(key);
        Iterator<Entry> iterator = cell.iterator();
        
        while (iterator.hasNext()) {
            Entry current = iterator.next();
            
            if (current.getKey() == key) {
                iterator.remove();
                this.numberOfElements --;
                return;
            }
        }
    }
    
    private List<Entry> getCell(int key) {
        int hashCode = key % this.hashTable.length;
        
        if (hashTable[hashCode] == null)
            hashTable[hashCode] = new LinkedList<>();
        
        return this.hashTable[hashCode];
    }
    
    
    private void rebuildHashTable() {
        if (this.numberOfElements < DEFAULT_SIZE * LOAD_FACTOR)
            return;
        
        List<Entry> oldTable = this.hashTable;
        this.hashTable = new List[oldTable.length * 2];
        
        for (List<Entry> row: oldTable) {
            for (Entry entry: row) {
                this.put(entry.getKey(), entry.getValue());
            }
        }
    } 
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
