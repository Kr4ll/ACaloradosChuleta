static class Node {
    int key;
    Node left, right;
    public Node(int item)
    {
        key = item;
        left = right = null;
    }
}
static class BinaryTree {
    // Root of Binary Tree
    Node root;
    BinaryTree() { root = null; }
    // Given a binary tree, print its nodes according to the
    // "bottom-up" postorder traversal.
    void printPostorder(Node node)
    {
        if (node == null)
            return;
        // First recur on left subtree
        printPostorder(node.left);
        // Then recur on right subtree
        printPostorder(node.right);
        // Now deal with the node
        System.out.print(node.key + " ");
    }
}
// Driver code
public static void main(String[] args)
{
    BinaryTree tree = new BinaryTree();
    tree.root = new Node(1);
    tree.root.left = new Node(2);
    tree.root.right = new Node(3);
    tree.root.left.left = new Node(4);
    tree.root.left.right = new Node(5);
    // Function call
    System.out.println(
        "Postorder traversal of binary tree is ");
    tree.printPostorder(tree.root);
}
