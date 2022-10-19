from array import array
from hexBLEndian import HexBlEndian

'''
Для перевірки моєї бібліотеки, я взяв тестові вектори з завдання.

для перевірки, достатньо запустити файл main.py, та на екран буде виведено необхідну інформацію

'''

Vector1 = "0xff00000000000000000000000000000000000000000000000000000000000000"
Vector2 = "0xaaaa000000000000000000000000000000000000000000000000000000000000"
Vector3 = "0xFFFFFFFF"
Vector4 = "0xF000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

Vector1_big = HexBlEndian.hextobig(Vector1,32)
Vector2_big = HexBlEndian.hextobig(Vector2,32)
Vector3_big = HexBlEndian.hextobig(Vector3,4)
Vector4_big = HexBlEndian.hextobig(Vector4,512)

Vector1_little = HexBlEndian.hextolittle(Vector1,32)
Vector2_little = HexBlEndian.hextolittle(Vector2,32)
Vector3_little = HexBlEndian.hextolittle(Vector3,4)
Vector4_little = HexBlEndian.hextolittle(Vector4,512)

Little_vector1 = HexBlEndian.littletohex(Vector1_little,32)
Little_vector2 = HexBlEndian.littletohex(Vector2_little,32)
Little_vector3 = HexBlEndian.littletohex(Vector3_little,4)
Little_vector4 = HexBlEndian.littletohex(Vector4_little,512)

Big_vector1 = HexBlEndian.bigtohex(Vector1_big,32)
Big_vector2 = HexBlEndian.bigtohex(Vector2_big,32)
Big_vector3 = HexBlEndian.bigtohex(Vector3_big,4)
Big_vector4 = HexBlEndian.bigtohex(Vector4_big,512)

print(f"результат роботи перетворення Hex на big/little значення:\n значення в hex: {Vector1} \n Значення в Big-Endian: {Vector1_big} \n Значення в Little-Endian: {Vector1_little} \n\n")
print(f"результат роботи Hex на big/little значення:\n значення в hex: {Vector2} \n Значення в Big-Endian: {Vector2_big} \n Значення в Little-Endian: {Vector2_little}\n\n")
print(f"результат роботи Hex на big/little значення:\n значення в hex: {Vector3} \n Значення в Big-Endian: {Vector3_big} \n Значення в Little-Endian: {Vector3_little}\n\n")
print(f"результат роботи Hex на big/little значення:\n значення в hex: {Vector4} \n Значення в Big-Endian: {Vector4_big} \n Значення в Little-Endian: {Vector4_little}\n\n")

print(f"результат роботи перетворення big/little в hex значення:\n значення в big-endian: {Vector1_big} --> Hex: {Big_vector1} \n Значення в Little-Endian: {Vector1_little} --> Hex: {Little_vector1} \n\n")
print(f"результат роботи перетворення big/little в hex значення:\n значення в big-endian: {Vector2_big} --> Hex: {Big_vector2} \n Значення в Little-Endian: {Vector2_little} --> Hex: {Little_vector2} \n\n")
print(f"результат роботи перетворення big/little в hex значення:\n значення в big-endian: {Vector3_big} --> Hex: {Big_vector3} \n Значення в Little-Endian: {Vector3_little} --> Hex: {Little_vector3} \n\n")
print(f"результат роботи перетворення big/little в hex значення:\n значення в big-endian: {Vector4_big} --> Hex: {Big_vector4} \n Значення в Little-Endian: {Vector4_little} --> Hex: {Little_vector4} \n\n")
