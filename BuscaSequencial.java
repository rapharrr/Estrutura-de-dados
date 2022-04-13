import java.util.Scanner;

class BuscaSequencial {
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
            System.out.print("\n");
            System.out.print("Digite o valor que deseja procurar: ");
            int x = input.nextInt();
            if (Busca(x, V)) {
                System.out.print("O número existe no vetor.");
            } else {
                System.out.print("O número não existe no vetor.");
            }
        }

    }

    public static boolean Busca(int x, int[] V) {
        for (int i = 0; i < V.length; i++) {
            if (x == V[i]) {
                return true;
            }
        }
        return false;
    }
}