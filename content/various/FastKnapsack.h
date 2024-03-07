#include <iostream>
#include <vector>
#include <algorithm> // Para max_element
using namespace std;
#define rep(i, a, b) for (int i = a; i < b; ++i)
#define vi vector<int>
int knapsack(vi w, int t) {
    int a = 0, b = 0, x;
    while (b < w.size() && a + w[b] <= t) a += w[b++];
    if (b == w.size()) return a;
    int m = *max_element(w.begin(), w.end());
    vi u, v(2*m, -1);
    v[a+m-t] = b;
    rep(i, b, w.size()) {
        u = v;
        rep(x, 0, m) v[x+w[i]] = max(v[x+w[i]], u[x]);
        for (x = 2*m; --x > m;) rep(j, max(0, u[x]), v[x])
            v[x-w[j]] = max(v[x-w[j]], j);
    }
    for (a = t; v[a+m-t] < 0; a--) ;
    return a;
}
int main() {
    // Ejemplo de entrada
    vi weights = {1, 1, 1, 1}; // Lista de pesos de los objetos
    int capacity = 7; // Capacidad máxima de la mochila
    // Llamada a la función knapsack
    int max_weight = knapsack(weights, capacity);
    cout << "El peso máximo que se puede llevar en la mochila es: " << max_weight << endl;
    return 0;
}
