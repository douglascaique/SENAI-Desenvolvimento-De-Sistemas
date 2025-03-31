package Praticas.ExercicioPoo;

public class MainLivro {
    public static void main(String[] args) {
        Livro livro1 = new Livro();

        livro1.setTitulo("Eragon");
        livro1.setAutor("Christopher Paolini");
        livro1.setnumPag(355);
        livro1.setPreco(21.90);


        System.out.println("Titulo: " + livro1.getTitulo());
        System.out.println("Autor: " + livro1.getAutor());
        System.out.println("Número de Páginas: " + livro1.getnumPag());
        System.out.println("Preço: " + livro1.getPreco());
    }
}
