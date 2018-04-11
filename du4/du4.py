from Crypto.Cipher import DES
start = 0x
def des( plaintext, key ):
  des = DES.new( key )
  return  des.encrypt( plaintext