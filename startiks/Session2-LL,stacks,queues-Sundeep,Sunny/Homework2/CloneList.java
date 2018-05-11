class Node {
    Node next;
    Node funny;
    int value;

    Node(int value) { this.value = value; }
}

class CloneList {
    static Node clone(Node list) {
        Map<Node, Node> map = new HashMap<>();

        Node n = list;
        while (n != null) {
            map.put(n, new Node(value));
            n = n.next;
        }

        Node n = list;
        while (n != null) {
            map.get(n).next = map.get(n.next);
            map.get(n).funny = map.get(n.funny);
            n = n.next;
        }

        return map.get(list);
    }
}