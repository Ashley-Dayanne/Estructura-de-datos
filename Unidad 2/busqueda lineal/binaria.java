public class binaria{
    public int busquedaBinaria(int [] arr, int x){
        int inicio=0;
        int fin= arr.length-1;

        while(inicio<=fin){
            int medio = inicio + (fin - inicio)/2;

            if(arr[medio] == x){
                return medio;
            }
            if(arr[medio]<x){
                
            }
        }
    }
}