def xor_cipher(s: str, key: int) -> str:
    # это можно было написать не использую ''.join,
    # но если вы дошли до этого задания, то разберётесь :)
    return ''.join([chr(ord(i) ^ key) for i in s])


# вот здесь хитрость, операция дешибрования аналогична операции шифрования
# То есть если вы сделаете операцию num ^ key ^ key вы всегда получите обратно num
# И да, в Python функции ялвляются объектами, и поэтому их можно просто присваивать
xor_uncipher = xor_cipher


my_secret_string = 'meaning of life is 42'
key = 7777
encrypted_string = xor_cipher(my_secret_string, key)
decrypted_string = xor_uncipher(encrypted_string, key)
print(my_secret_string)  # meaning of life is 42
print(encrypted_string)  # ḌḄḀḏḈḏḆṁḎḇṁḍḈḇḄṁḈḒṁṕṓ
print(decrypted_string)  # meaning of life is 42
