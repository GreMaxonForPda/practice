public class Tickets {
    public static void main(String[] args) {
        System.out.println("Использование цикла for:");
        for (int i = 2000; i < 2101; i++) {
            System.out.println("    Билет номер " + i);
        }
        System.out.println("Использование цикла while:");
        int i = 2200;
        while (i < 2351) {
            System.out.println("    Билет номер " + i);
            i++;
        }
    }
}
