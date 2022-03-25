
public class Loader
{
    public static void main(String[] args)
    {
        Cat cat = new Cat();
        Cat cat2 = new Cat();

        while (cat.getWeight() < 9002) {
            cat.feed(500.0);
            System.out.println(cat.getStatus());
            System.out.println("    Вес кошки равен " + cat.getWeight());
        }
        while (cat2.getWeight() > 1000) {
            cat2.meow();
            System.out.println(cat2.getStatus());
            System.out.println("    Вес кошки равен " + cat2.getWeight());
        }
    }
}