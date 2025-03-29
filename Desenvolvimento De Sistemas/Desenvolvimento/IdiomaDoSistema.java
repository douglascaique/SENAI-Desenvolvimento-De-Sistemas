package Desenvolvimento;

import java.util.Locale;

public class IdiomaDoSistema {
    public static void main(String[] args) {
        Locale idioma =  Locale.getDefault();

        System.out.println("O idioma do sistema é: " + idioma.getDisplayLanguage());
        System.out.println("Código do idioma: " + idioma.getLanguage());
    }
}
