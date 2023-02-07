// class for message, which provides a secure object to keep the message, even when intercepted, the shift number is kept hidden
public class Message {
    String message;
    boolean isEncrypted; 

    // constructor declaration to initialize variables
    public Message(String message, boolean isEncrypted) {
        this.message = message;
        this.isEncrypted = isEncrypted;
    }

    // method for encode/decode message with caesar cipher
    public String caesarCipherMsg(Message msg, int shift) {
        CaesarCipher cipherMsg = new CaesarCipher();
        String newMsg = "";
        if (msg.isEncrypted == true) {
            newMsg = cipherMsg.encryptData(msg, shift);
            // return new message 
            return newMsg;
        }
        else if (msg.isEncrypted == false) {
            newMsg = cipherMsg.decodeData(msg, shift);
            // return new message
            return newMsg;
        }
        else {
            return "";
        }
    }
}