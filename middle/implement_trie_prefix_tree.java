// 208. 实现 Trie (前缀树)
// https://leetcode-cn.com/problems/implement-trie-prefix-tree/
class Trie {
    Node[] firstNode = new Node[26];

    class Node {
        Node[] children = new Node[26];
        boolean isEnd;
    }

    /**
     * Initialize your data structure here.
     */
    public Trie() {
    }

    /**
     * Inserts a word into the trie.
     */
    public void insert(String word) {
        Node[] floor = firstNode;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (floor[c - 97] == null) {
                floor[c - 97] = new Node();
            }
            if (i < word.length() - 1) {
                floor = floor[c - 97].children;
            } else {
                floor[c - 97].isEnd = true;
            }
        }
    }

    /**
     * Returns if the word is in the trie.
     */
    public boolean search(String word) {
        Node[] floor = firstNode;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (floor == null || floor[c - 97] == null) {
                return false;
            }

            if (i == word.length() - 1 && floor[c - 97].isEnd) {
                return true;
            }
            floor = floor[c - 97].children;
        }
        return false;
    }

    /**
     * Returns if there is any word in the trie that starts with the given prefix.
     */
    public boolean startsWith(String prefix) {
        Node[] floor = firstNode;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if (floor == null || floor[c - 97] == null) {
                return false;
            }
            floor = floor[c - 97].children;
        }
        return true;
    }

    public static void main(String[] args) {
        Trie obj = new Trie();
        String word = "aleet";
        obj.insert(word);
        boolean param_2 = obj.search(word);
        boolean param_3 = obj.startsWith("lee");
        System.out.println(param_2);
        System.out.println(param_3);
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
//["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"];
//        [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]