// class for caesar cipher, which encodes and decodes messages w/shift
public class CaesarCipher {   
    // encrypt data 
    public static String encryptData(Message msg, int shift) {   
        // variables
        String encodedMsg = "";
        // checks if shift is above 26, then divides and gets remainder 
        if (shift > 26) {
            shift = shift % 26;
        }
        else if (shift < 0) {
            shift = (shift % 26) + 26;
        }
        // for loop to encrypt every char of given message  
        for (int i = 0; i < msg.message.length(); i++) {   
            char letter = msg.message.charAt(i);
            if (Character.isLetter(letter)) {
                if (Character.isLowerCase(letter)) {
                    // shifting character, now we have to figure out which letter it is
                    char shiftedChar = (char)(letter + shift);
                    if (shiftedChar > 'z') {
                        encodedMsg += (char)(shiftedChar - (26 - shift));
                    }
                    else {
                        encodedMsg += shiftedChar;
                    }
                }
                else if (Character.isUpperCase(letter)) {
                    // shifting character, now we have to figure out which letter it is
                    char shiftedChar = (char)(letter + shift);
                    if (shiftedChar > 'Z') {
                        encodedMsg += (char)(shiftedChar - (26 - shift));
                    }
                    else {
                        encodedMsg += shiftedChar;
                    }
                }
            }
            else {
                // maybe a symbol or number idk
                encodedMsg += letter; 
            }
        }
        // return the new message
        return encodedMsg;
    }   

    // decode data 
    public static String decodeData(Message msg, int shift) {   
        // variables
        String decodedMsg = "";
        // checks if shift is above 26, then divides and gets remainder 
        if (shift > 26) {
            shift = shift % 26;
        }
        else if (shift < 0) {
            shift = (shift % 26) + 26;
        }
        // for loop to decode every char of given message  
        for (int i = 0; i < msg.message.length(); i++) {   
            char letter = msg.message.charAt(i);
            if (Character.isLetter(letter)) {
                if (Character.isLowerCase(letter)) {
                    // shifting character, now we have to figure out which letter it is
                    char shiftedChar = (char)(letter - shift);
                    if (shiftedChar < 'a') {
                        decodedMsg += (char)(shiftedChar + (26 - shift));
                    }
                    else {
                        decodedMsg += shiftedChar;
                    }
                }
                else if (Character.isUpperCase(letter)) {
                    // shifting character, now we have to figure out which letter it is
                    char shiftedChar = (char)(letter - shift);
                    if (shiftedChar < 'A') {
                        decodedMsg += (char)(shiftedChar + (26 - shift));
                    }
                    else {
                        decodedMsg += shiftedChar;
                    }
                }
            }
            else {
                // maybe a symbol or number idk
                decodedMsg += letter; 
            }
        }
        // return the new message
        return decodedMsg;
    }  
}