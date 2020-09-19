class ListNode {
    String url;
    ListNode next = null;
    ListNode prev = null;
    
    public ListNode(String url) {
        this.url = url;
    }
}

class BrowserHistory {
    
    ListNode current;
    
    public BrowserHistory(String homepage) {
        this.current = new ListNode(homepage);
    }
    
    public void visit(String url) {
        ListNode node = new ListNode(url);
        current.next = node;
        node.prev = current;
        current = current.next;
    }
    
    public String back(int steps) {
        while (steps > 0 && current.prev != null) {
            current = current.prev;
            steps -= 1;
        }
        return current.url;    
    }
    
    public String forward(int steps) {
        while (steps > 0 && current.next != null) {
            current = current.next;
            steps -= 1;
        }
        return current.url;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */
