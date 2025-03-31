package Praticas.Exercicios;

import java.util.Scanner;

public class MediaAluno {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Lê o nome do aluno
        System.out.print("Digite o nome do aluno: ");
        String nome = scanner.nextLine();

        // Lê as notas das duas provas
        System.out.print("Digite a nota da primeira prova: ");
        double nota1 = scanner.nextDouble();

        System.out.print("Digite a nota da segunda prova: ");
        double nota2 = scanner.nextDouble();

        // Calcula a média aritmética
        double media = (nota1 + nota2) / 2;

        // Exibe o nome e a média do aluno
        System.out.println("\nNome do aluno: " + nome);
        System.out.println("Média aritmética: " + media);

        // Verifica se o aluno está reprovado
        if (media < 7) {
            System.out.println("Status: Reprovado");
        } else {
            System.out.println("Status: Aprovado");
        }

        scanner.close();
    }
}
