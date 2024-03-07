import java.io.*;
public class Main {
    private int length;
    private long mod1 = (long) 1e9 + 7;
    private long mod2 = (long) 1e9 + 9;
    private int p1 = 31;
    private int p2 = 37;
    private long[] hash1;
    private long[] hash2;
    public Main(String s) {
        length = s.length();
        hash1 = new long[length];
        hash2 = new long[length];
        // Compute hashes of the string s
        long h1 = 0, h2 = 0;
        long p_pow1 = 1, p_pow2 = 1;
        for (int i = 0; i < length; i++) {
            h1 = (h1 + (s.charAt(i) - 'a' + 1) * p_pow1) % mod1;
            h2 = (h2 + (s.charAt(i) - 'a' + 1) * p_pow2) % mod2;
            p_pow1 = (p_pow1 * p1) % mod1;
            p_pow2 = (p_pow2 * p2) % mod2;
            hash1[i] = h1;
            hash2[i] = h2;
        }
    }
    // Returns the hash value of the prefix of s up to index i
    public Pair<Long, Long> prefix(int index) {
        return new Pair<>(hash1[index], hash2[index]);
    }
    // Returns the hash value of the substring of s from index l to r (inclusive)
    public Pair<Long, Long> substr(int l, int r) {
        if (l == 0) {
            return new Pair<>(hash1[r], hash2[r]);
        }
        long temp1 = (hash1[r] - hash1[l - 1] + mod1) % mod1;
        long temp2 = (hash2[r] - hash2[l - 1] + mod2) % mod2;
        temp1 = (temp1 * modInverse(p1, length - l, mod1)) % mod1;
        temp2 = (temp2 * modInverse(p2, length - l, mod2)) % mod2;
        return new Pair<>(temp1, temp2);
    }
    private long modInverse(long base, long exp, long mod) {
        long result = 1;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp /= 2;
        }
        return result;
    }
    // Override equals method to compare two RollingHash objects
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        GFG other = (GFG) obj;
        return prefix(length - 1).equals(other.prefix(other.length - 1));
    }
    public static void main(String[] args) {
        String myStr = "geeksforgeeks";
        Main hash = new Main(myStr);
        Pair<Long, Long> hashPair = hash.substr(0, myStr.length() - 1);
        System.out.println("Hashes of the string " + myStr + " are:");
        System.out.println(hashPair);
    }
}
// Pair class to hold two values together
class Pair<T, U> {
    private T first;
    private U second;
 
    public Pair(T first, U second) {
        this.first = first;
        this.second = second;
    }
    @Override
    public String toString() {
        return "(" + first + ", " + second + ")";
    }
}
