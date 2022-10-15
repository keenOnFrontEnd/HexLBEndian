import binascii

class HexBlEndian:
  @classmethod
  def hextolittle(self,value,size):
    try:
        if(value[0] == "0" and value[1] == 'x'):
             convertedHex = value[2:]
        else:
             convertedHex = value
    except Exception:
        raise Exception("Input data must be of the string type")
    hex = convertedHex  + "0"*(size*2 - len(convertedHex))
    result = int.from_bytes(binascii.unhexlify(hex),byteorder='little')
    return result
  @classmethod
  def hextobig(self,value,size):
    try:
        if(value[0] == "0" and value[1] == 'x'):
             convertedHex = value[2:]
        else:
             convertedHex = value
    except Exception:
        raise Exception("Input data must be of the string type")
    hex = convertedHex  + "0"*(size*2 - len(convertedHex))
    result = int.from_bytes(binascii.unhexlify(hex),byteorder='big')
    return result
  @classmethod
  def littletohex(self,value,size):
    try:
       convertedValue = int.to_bytes(value,size,byteorder='little')
    except Exception:
        raise Exception("Input data must be of the integer type")
    hex = binascii.hexlify(convertedValue)
    return "0x" + str(hex,"utf-8").strip("0")
  @classmethod
  def bigtohex(self,value,size):
    try:
       convertedValue = int.to_bytes(value,size,byteorder='big')
    except Exception:
        raise Exception("Input data must be of the integer type")
    hex = binascii.hexlify(convertedValue)
    return "0x" + str(hex,"utf-8").strip("0")