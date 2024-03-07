public class Main {
    public static long mulMod(long a, long b, long mod)
    {
        long res = 0;
        while (b > 0) {
            if ((b & 1) == 1) {
                res = (res + a) % mod;
            }
            a = (a * 2) % mod;
            b >>= 1;
        }
        return res;
    }
    public static long powMod(long a, long b, long mod){
        long res = 1;
        a %= mod;
        while (b > 0) {
            if ((b & 1) == 1) {
                res = mulMod(res, a, mod);
            }
            a = mulMod(a, a, mod);
            b >>= 1;
        }
        return res;}
    public static long barrettReduce(long x, long mod,
                                     long mu){
        long q1 = x >> 32;
        long q2 = ((mu * q1) >> 32) * mod;
        long r1 = x & 0xffffffff;
        long r2 = mu * r1;
        long q3 = r2 >> 32;
        long r3 = r1 - q3 * mod;
        long res = r3 + ((r3 >> 63) & mod);
        if (res >= mod) {
            res -= mod;
        }
        return res;
    }
    public static void main(String[] args)
    {
        long xSquared = mulMod(x, x, mod);
        long xSquaredBarrett
            = barrettReduce(xSquared, mod, mu);
        long xPow1234 = powMod(x, 1234, mod);
        long xPow1234Barrett
            = barrettReduce(xPow1234, mod, mu);
    }
}
