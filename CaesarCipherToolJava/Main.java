// libraries 
import java.util.Scanner;   
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        // intro
        System.out.println("hello this is the java cipher tool");
        // variables
        int shift = 0;
        boolean isEncrypted = false;
        // scan for user input 
        Scanner scan = new Scanner(System.in);
        System.out.println("what is your message?");
        String originalMessage = scan.nextLine();
        // check if user input is empty
        while (true) {
            if (originalMessage.isEmpty()) {
                System.out.println("couldn't read your message. try again.");
                originalMessage = scan.nextLine();
            }
            else {
                break;
            }
        }
        // prompt user if they would like to encode or decode 
        System.out.println("your message is: " + originalMessage);
        System.out.println("would you like to encrypt or decode your message? (e/d)");
        String userInput = scan.nextLine();	
        // loop to check for user input 
        while (true) {
            // encode 
            if (userInput.equals("e")) {
                isEncrypted = true; 
                // prompt user for shift 
                System.out.println("pick a number for your shift.");
                // randomize shift (for more security)
                System.out.println("if you want to, you can randomize your shift between 0-100 by typing 'randomize'.");
                boolean checkInt = scan.hasNextInt();
                userInput = scan.nextLine();
                // randomize shift number 
                if (userInput.equals("randomize")) {
                    Random random = new Random();
                    shift = random.nextInt(101);
                    System.out.println("Your randomized shift number is: " + Integer.toString(shift));
                    // begin converting into cipher 
                    Message msg = new Message(originalMessage, isEncrypted);
                    String newMsg = msg.caesarCipherMsg(msg, shift);
                    System.out.println("your encoded message w/shift of " + Integer.toString(shift) + " is " + newMsg);
                    break;
                }
                // could not read message or message is correct
                else {
                    if (userInput.isEmpty()) {
                        System.out.println("couldn't read your message. try again.");
                        userInput = scan.nextLine();
                    }
                    else {
                        if (checkInt && Integer.parseInt(userInput) > 0) {
                            // begin converting into cipher 
                            shift = Integer.parseInt(userInput);
                            System.out.println("your shift number is: " + Integer.toString(shift));
                            Message msg = new Message(originalMessage, isEncrypted);
                            String newMsg = msg.caesarCipherMsg(msg, shift);
                            System.out.println("your encoded message w/shift of " + Integer.toString(shift) + " is " + newMsg);
                            break;
                        }
                        else {
                            System.out.println("couldn't read your message. type in a whole number more than 0.");
                            userInput = scan.nextLine();
                        }
                    }
                }
            }
            // decode 
            else if (userInput.equals("d")) {
                isEncrypted = false; 
                // prompt user for shift 
                System.out.println("what was your shift?");
                boolean checkInt = scan.hasNextInt();
                userInput = scan.nextLine();
                // could not read message or message is correct
                if (userInput.isEmpty()) {
                    System.out.println("couldn't read your message. try again.");
                    userInput = scan.nextLine();
                }
                else {
                    if (checkInt && Integer.parseInt(userInput) > 0) {
                        // begin converting into cipher 
                        shift = Integer.parseInt(userInput);
                        System.out.println("your shift number is: " + Integer.toString(shift));
                        Message msg = new Message(originalMessage, isEncrypted);
                        String newMsg = msg.caesarCipherMsg(msg, shift);
                        System.out.println("your decoded message w/shift of " + Integer.toString(shift) + " is " + newMsg);
                        break;
                    }
                    else {
                        System.out.println("couldn't read your message. type in a whole number");
                        userInput = scan.nextLine();                    
                    }
                }
            }    
            // default 
            else {
                System.out.println("couldn't read your message. Type in 'e' to encode or 'd' to decode a message.");
                userInput = scan.nextLine();
                continue;
            }
        }
    }
}