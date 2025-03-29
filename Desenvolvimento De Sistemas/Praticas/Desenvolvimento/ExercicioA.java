package Praticas.Desenvolvimento;

import javax.sound.sampled.SourceDataLine;

public class ExercicioA {
    public static void main(String[] args) {
    // variáveis
    int prestacoes = 5;
    double valor = 150.500;

    // divisão
    double prestacao = valor / prestacoes;

    System.out.println("O valor R$ " + valor + ", pode ser dividido em até 5x de " + prestacao);
    }



}