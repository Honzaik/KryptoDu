import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Arrays;
import java.util.HashMap;

public class main {

    static int counter = 0;
    static HashMap<String, Integer> nagenerovaneHodnoty;

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

    private static byte[] getNextKey(){
        byte[] bs = ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(counter).array(); //nageneruje klíč příslušný číslu counter
        bs = Arrays.copyOf(bs, 3);
        while(!isOdd(bs)){ //zkontroluj jestli je lichý
            counter++;
            bs = ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(counter).array();
            bs = Arrays.copyOf(bs, 3);
        }
        counter++;
        byte[] newKey = Arrays.copyOf(bs,8);
        for(int i = 3; i < 8; i++){ //dopln zbylé 01...
            newKey[i] = 1;
        }
        return newKey;
    }

    private static String byteToString(byte[] input){ //převede pole bytů do stringu pro jednoduché porovnávání v hashmapě, klidně by to šlo do longintu apod...
        String result = "";
        for(byte b : input){
            result += Byte.toUnsignedInt(b) + "|";
        }
        return result;
    }

    public static void main(String[] args) {
        nagenerovaneHodnoty = new HashMap();
        byte[] plaintext = new byte[]{0,1,2,3,4,5,6,7};
        byte[] ciphertext = new byte[]{(byte)0xb0,(byte)0x20,(byte)0x23,(byte)0x51,(byte)0xd7,(byte)0xe,(byte)0xaf,(byte)0xd7};
        byte[] enc = null;
        byte[] key = null;
        String s = null;

        long timeStart = System.currentTimeMillis();
        while(counter < 16711423){ //"nejvetsi" lichý klic je 16711422
            key = getNextKey();
            try {
                enc = DES.Encrypt(plaintext, key);
                s = byteToString(enc);
                nagenerovaneHodnoty.put(s, counter - 1); //ulož nagenerovaný ciphertext společně s danou hodnotou counter, ze kterého je klíč vygenerován
            }catch (Exception e){
                e.printStackTrace();
            }
        }
        System.out.println("nagenerovan plaintext za " + (System.currentTimeMillis()-timeStart) ); //zpráva, že skončila 1. část útoku
        timeStart = System.currentTimeMillis();
        counter = 0;
        while(counter < 16711423){
            key = getNextKey();
            try {
                s = byteToString(DES.Encrypt(ciphertext, key));
                if(nagenerovaneHodnoty.containsKey(s)){
                    System.out.println("NAŠEL JSEM SHODU");
                    System.out.println(s); //shoda
                    System.out.println(counter-1); //vrať příslušný klíč b
                    System.out.println(nagenerovaneHodnoty.get(s)); //vrať příslušný klíč a
                    break;
                }
            }catch (Exception e){
                e.printStackTrace();
            }
        }
        System.out.println((System.currentTimeMillis()-timeStart) + " " + counter);

        //text 88|237|175|46|204|135|182|218 - shoda v decimalni soustave
        int keyA = 460551;
        int keyB = 723723;
        counter = 460551;
        byte[] keys1 = getNextKey(); //vrati klic A
        counter = 723723;
        byte[] keys2 = getNextKey(); //vrati klic B
        System.out.print("a: ");
        for (byte b : keys1){
            System.out.format("0x%02x ", b);
        }
        System.out.println();
        System.out.print("b: ");
        for (byte b : keys2){
            System.out.format("0x%02x ", b);
        }


    }
}
