  GNU nano 6.2                                                                                        KitchenKit.h                                                                                                 
/**
 * Author: Diego 
 * License: CC0
 * Source: Codeforces
 * Description: FastReader para inputs en java
 * Time: no time
 * Status: tested on http://codeforces.com/contest/321/problem/E
 */
#pragma once

 static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        
        public FastReader() {
            br = new BufferedReader(
                    new InputStreamReader(System.in));
        }
        
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        int nextInt() { // 10^9
            return Integer.parseInt(next());
        }
        
        long nextLong() { // 10^18
            return Long.parseLong(next());
        }
        
        double nextDouble() {
            return Double.parseDouble(next());
        }
        
        BigInteger nextBigInteger() {
            return new BigInteger(next());
        }
        
        String nextLine() {
            String str = "";
            try {
                if (st != null && st.hasMoreTokens()) {
                    str = st.nextToken("\n");
                } else {
                    str = br.readLine();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
        
        Map.Entry<Boolean, Optional<String>> hasNext() {
            try {
                String line = br.readLine();
                return Map.entry(line != null, Optional.ofNullable(line));
            } catch (IOException e) {
                e.printStackTrace();
                return Map.entry(false, Optional.of(""));
            }
        }
        
        void close() {
            try {
                br.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
    }
