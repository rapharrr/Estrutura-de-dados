import java.util.Scanner;

class BuscaBinaria {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            int V[];
            V = new int[5]; // muda o tamanho do vetor
            int modulo = V.length;
            for (int i = 0; i < V.length; i++) { // coloca os dados dentro do vetor
                V[i] = modulo;
                modulo = modulo - 1;
            }

            for (int i = 0; i < V.length; i++) { // imprime o vetor desordenado
                System.out.print(V[i] + " ");
            }
            System.out.print("Digite o valor que deseja procurar: ");
            int x = input.nextInt();
            System.out.print("O número procurado está na posição " + Busca(x, V, 0, V.length) + " do vetor");

            System.out.print("\n");
            for (int i = 0; i < V.length; i++) { // imprime o vetor ordenado
                System.out.print(V[i] + " ");
            }
        }
    }

    public static int Busca(int x, int[] V, int p, int r) {
        if (p > r) {
            return -1;
        } else {
            int q = (p + r) / 2;
            if (V[q] == x) {
                return q;
            } else if (V[q] > x) {
                return Busca(x, V, (q + 1), r);
            } else {
                return Busca(x, V, p, (q - 1));
            }
        }
    }
}