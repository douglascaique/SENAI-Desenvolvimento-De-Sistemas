package Praticas.Exercicios;

import java.util.Scanner;

public class MediaAluno2 {
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
        double media = calculaMedia(nota1, nota2);

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


    public static String statusAluno(double media) {

        if (media >= 7){
            return "Aprovado";
        } else if (media >= 5 && media <7) {
            return "Verificação Suplementar";
        } else{
            return "Reprovado";
        }
    };

    public static Double calculaMedia(double nota1, double nota2) {
        return (nota1 + nota2) / 2;
    }
}
