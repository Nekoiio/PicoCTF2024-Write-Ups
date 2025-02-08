a = 94
b = 29
g = 31
p = 97
text_key = "trudeau"
cipher_list =[260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]
#change the values above to match yours
u = pow(g,a) % p
v = pow(g,b) % p
key = pow(v,a) % p
b_key = pow(u,b) % p
shared_key = None
if key == b_key:
  shared_key = key
else:
  print("invalid key")
  
def enc_reverse(cipher_list, key):
    reversed_list = []
    for i in cipher_list:
        reversed_list.append(chr(i // (key * 311)))

    reversed_str = ''.join(reversed_list)
    print(reversed_str)
    return reversed_str
semi = enc_reverse(cipher_list,shared_key)
def reverse_dynamic_xor(cipher_text, text_key):
    decrypted_text = ""
    key_length = len(text_key)
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted_text += decrypted_char
    return decrypted_text
full = reverse_dynamic_xor(semi,text_key)
print(full[::-1])
