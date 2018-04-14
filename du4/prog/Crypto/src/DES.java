import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;

class DES
{
    public static byte[] Encrypt( byte[] plaintext, byte[] key ) throws Exception
    {
        Cipher des = Cipher.getInstance("DES/ECB/NoPadding");
        des.init( Cipher.ENCRYPT_MODE, SecretKeyFactory.getInstance("DES").generateSecret( new DESKeySpec( key ) ) );
        return des.doFinal( plaintext );
    }
}