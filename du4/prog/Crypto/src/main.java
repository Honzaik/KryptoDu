import javax.sound.midi.Soundbank;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class main {

    static int counter = 0;
    static HashMap<String, Integer> values1;

    private static boolean isOdd(byte[] bytes){
        boolean result = true;
        for(int i = 0; i < 3; i++){
            int pocetJednicek = 0;
            for(int j = 0; j < 8; j++){
                if((bytes[i] & (1 << j))  > 0){
                    pocetJednicek++;
                }
            }
            if((pocetJednicek % 2 == 0)){
                result = false;
                break;
            }
        }
        return result;
    }
    /*
    private static void reverse(byte[] input){
        for(int i = 0; i < input.length/2; i++){
            byte temp = input[i];
            input[i] = input[input.length-1-i];
            input[input.length-1-i] = temp;
        }
        //return input;
    }*/

    private static byte[] getNextKey(){
        byte[] bs = ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(counter).array();
        bs = Arrays.copyOf(bs, 3);
        while(!isOdd(bs)){
            counter++;
            bs = ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(counter).array();
            bs = Arrays.copyOf(bs, 3);
        }
        counter++;
        byte[] newKey = Arrays.copyOf(bs,8);
        for(int i = 3; i < 8; i++){
            newKey[i] = 1;
        }
        return newKey;
    }

    /*private static boolean hasKey(byte[] input){
        Iterator it = values1.entrySet().iterator();
        while(it.hasNext()) {
            Map.Entry pair = (Map.Entry) it.next();
            if(Arrays.equals((byte[])pair.getKey(), input)){
                return true;
            }
        }
        return false;
    }*/

    private static String byteToString(byte[] input){
        String result = "";
        for(byte b : input){
            result += Byte.toUnsignedInt(b) + "|";
        }
        return result;
    }

    public static void main(String[] args) {
        values1 = new HashMap();
        byte[] plaintext = new byte[]{(byte)0x0,(byte)0x1,(byte)0x2,(byte)0x3,(byte)0x4,(byte)0x5,(byte)0x6,(byte)0x7};
        //byte[] plaintext = new byte[]{7,6,5,4,3,2,1,0};
        byte[] ciphertext = new byte[]{(byte)0xb0,(byte)0x20,(byte)0x23,(byte)0x51,(byte)0xd7,(byte)0xe,(byte)0xaf,(byte)0xd7};
        //byte[] ciphertext = new byte[]{(byte)0xd7,(byte)0xaf,(byte)0xe,(byte)0xd7,(byte)0x51,(byte)0x23,(byte)0x20,(byte)0xb0};
        byte[] enc = null;
        byte[] key = null;
        String s = null;
        /*
        long timeStart = System.currentTimeMillis();
        while(counter < 16711423){
            key = getNextKey();
            try {
                enc = DES.Encrypt(plaintext, key);
                s = byteToString(enc);
                values1.put(s, counter - 1);
            }catch (Exception e){
                e.printStackTrace();
            }
        }
        System.out.println("nagenerovan plaintext " + values1.size() + " " + (System.currentTimeMillis()-timeStart) );
        /*
        for(byte b : key){
            //System.out.format("0x%02x ", b);
        }
        System.out.println();
        Iterator it = values1.entrySet().iterator();
        while(it.hasNext()){
            Map.Entry pair = (Map.Entry)it.next();
            System.out.print(pair.getValue() + ": ");
            for(byte b : (byte[])pair.getKey()){
                System.out.format("0x%02x ", b);
            }
            System.out.println();
        }


        System.out.println();
        System.out.println();
        timeStart = System.currentTimeMillis();
        counter = 0;
        while(counter < 16711423){
            key = getNextKey();
            try {
                s = byteToString(DES.Encrypt(ciphertext, key));
                if(values1.containsKey(s)){
                    System.out.println("FOUND ONE");
                    System.out.println(s);
                    System.out.println(counter-1);
                    System.out.println(values1.get(s));
                    break;
                }
            }catch (Exception e){
                e.printStackTrace();
            }
            //System.out.println(counter);
        }
        System.out.println((System.currentTimeMillis()-timeStart) + " " + counter);
        */
        //text 88|237|175|46|204|135|182|218|
        int key2 = 723723;
        int key1 = 460551;
        counter = 460551;
        byte[] keys1 = getNextKey();
        counter = 723723;
        byte[] keys2 = getNextKey();
        for (byte b : keys1){
            System.out.format("0x%02x ", b);
        }
        System.out.println();
        System.out.println();
        for (byte b : keys2){
            System.out.format("0x%02x ", b);
        }
        try {
            byte[] enc1 = DES.Encrypt(plaintext, keys1);
            byte[] enc2 = DES.Encrypt(ciphertext, keys2);
            System.out.println();
            for (byte b : enc1){
                System.out.format("0x%02x ", b);
            }
            System.out.println();
            System.out.println();
            for (byte b : enc2){
                System.out.format("0x%02x ", b);
            }
        } catch (Exception e){
            e.printStackTrace();
        }


    }
}
