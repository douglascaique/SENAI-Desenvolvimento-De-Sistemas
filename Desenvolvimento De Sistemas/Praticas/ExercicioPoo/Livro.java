package Praticas.ExercicioPoo;

public class Livro {
    private String titulo;
    private String autor;
    private int numPag;
    private double preco;




    public String getTitulo(){
        return titulo;
    }

    public String getAutor(){
        return autor;
    }
    public int getnumPag(){
        return numPag;
    }
    public double getPreco(){
        return preco;
    }


    public void setTitulo(String titulo){
        this.titulo = titulo;
    }
    public void setAutor(String autor){
        this.autor = autor;
    }
    public void setnumPag(int numPag){
        this.numPag = numPag;
    }
    public void setPreco(double preco){
        this.preco = preco;
    }

    // 
    // public Livro(String titulo, String autor, int numPag, double preco) {
    //     this.titulo = titulo;
    //     this.autor = autor;
    //     this.numPag = numPag;
    //     this.preco = preco;
    // }
    
}
