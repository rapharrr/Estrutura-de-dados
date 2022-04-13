class Main {
    public static void main(String[] args) {
          int V[];
      V = new int[5]; //muda o tamanho do vetor
      int modulo = V.length;
      for(int i=0; i < V.length; i++){ //coloca os dados dentro do vetor
        V[i] = modulo;
        modulo = modulo - 1;
        }
      for(int i=0; i<V.length; i++){ //imprime o vetor desordenado
        System.out.print(V[i] + " ");
      }
      
      V = QuickSort(V, 0, 4);
      System.out.print("\n");
      for(int i=0; i<V.length; i++){ //imprime o vetor desordenado
        System.out.print(V[i] + " ");
      }
      }
      
      public static int[] QuickSort(int[] V, int p, int r){
          if(p < r){
              int q = Partition(V, p, r);
              QuickSort(V, p, (q-1));
              QuickSort(V, q, r);
          }
          return V;
          }
          
      public static int Partition(int[] V, int p, int r){
          int x = V[r];
          int i = (p-1);
          for(int j = p;j < r;j++){
              if(V[j] <= x){
                  i = i+1;
                  int temp = V[i];
                  V[i] = V[j];
                  V[j] = temp;
              }
          }
          int aux = V[i+1];
              V[i+1] = V[r];
              V[r] = aux;
          return (i+1);
      }
  }