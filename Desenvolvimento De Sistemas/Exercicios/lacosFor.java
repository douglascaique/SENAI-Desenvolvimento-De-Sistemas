package exercicios;

import java.util.Scanner;

public class lacosFor {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        System.out.println("Digite sua idade:");
        int idade = ler.nextInt();
        
        while(idade<18){
            System.out.println("Acesso Negado.");
            System.out.println("Digite sua idade: ");
            idade = ler.nextInt();
        }

        System.out.println("Acesso permitido.");
        System.out.println("Carregando...");
    }
}
