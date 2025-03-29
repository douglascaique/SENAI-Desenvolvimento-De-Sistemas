package Desenvolvimento;

import java.awt.Dimension;
import java.awt.Toolkit;
import java.util.Locale;

public class ResolucaoTela {
    public static void main(String[] args) {
        Dimension resolucaoTela = Toolkit.getDefaultToolkit().getScreenSize();

        System.out.println("Sua tela tem resolução " + resolucaoTela.width + "X" + resolucaoTela.height);
    }
}
