public class Ages {
    public static void main(String[] args) {

        int myAge = 17;
        int yourAge = 39;
        int anonimAge = 35;

        int min = -1;
        int max = -1;
        int middle = -1;

        if (myAge > yourAge && yourAge > anonimAge) {
            middle = yourAge;
            max = myAge;
            min = anonimAge;
        }
        else if (yourAge > myAge && myAge > anonimAge) {
            middle = myAge;
            max = yourAge;
            min = anonimAge;
        }
        else if (anonimAge > yourAge && yourAge > myAge) {
            middle = yourAge;
            max = anonimAge;
            min = myAge;
        }
        else if (yourAge > anonimAge && anonimAge > myAge) {
            middle = anonimAge;
            max = yourAge;
            min = myAge;
        }
        else if (myAge > anonimAge && anonimAge > yourAge) {
            middle = anonimAge;
            max = myAge;
            min = yourAge;
        }
        else if (anonimAge > myAge && myAge > yourAge) {
            middle = myAge;
            max = anonimAge;
            min = yourAge;
        }
        System.out.println("Максимальный возраст: " + max + "\nСредний возраст: " + middle + "\nМинимальный возраст: " + min);
    }
}
