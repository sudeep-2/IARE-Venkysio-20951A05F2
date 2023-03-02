public class ReverseString {
public static String reverse(String str) {
        if (str.isEmpty()) {
            return str;
        }
        // recursive case
        else {
            return reverse(str.substring(1)) + str.charAt(0);
        }
    }
    public static void main(String[] args) {
        String str ="sudeep";
        System.out.println(reverse(str)); // prints "dlrow olleh"
    }
}
