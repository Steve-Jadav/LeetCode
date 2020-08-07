class Entry {
    private int key;
    
    public Entry(int key) {
        this.key = key;
    }
    
    public int getKey() {
        return this.key;
    }
}

class MyHashSet {
    
    private final int DEFAULT_SIZE = 10000;
    private int numberOfItems;
    private List<Entry>[] hashSet;
    
    /** Initialize your data structure here. */
    public MyHashSet() {
        this.hashSet = new List[DEFAULT_SIZE]; 
        this.numberOfItems = 0;
    }
    
    public void add(int key) {
        List<Entry> cell = getCell(key);
        
        for (Entry entry: cell) {
            if (entry.getKey() == key)
                return;
        }
        
        this.numberOfItems += 1;
        cell.add(new Entry(key));
    }
    
    public void remove(int key) {
        List<Entry> cell = getCell(key);
        Iterator<Entry> iterator = cell.iterator();
        
        while (iterator.hasNext()) {
            Entry current = iterator.next();
            
            if (current.getKey() == key) {
                iterator.remove();
                this.numberOfItems -= 1;
                return;
            }
        }
        
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        List<Entry> cell = getCell(key);
        
        for (Entry entry: cell) {
            if (entry.getKey() == key)
                return true;
        }
        
        return false;
    }
    
    private List<Entry> getCell(int key) {
        int hashCode = key % this.hashSet.length;
        
        if (this.hashSet[hashCode] == null)
            this.hashSet[hashCode] = new LinkedList<>();
        
        return this.hashSet[hashCode];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
