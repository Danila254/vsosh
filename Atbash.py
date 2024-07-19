class Atbash:
    def encrypt(text):
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧШЩЪЫЬЭЮЯ'
        alpha = 'абвгдеёжзийклмнопрстуфхчшщъыьэюя'
        result = ""
        for i in text:
            if i.islower():
                result += Atbash.func(i)
            else:
                result += Atbash.funcC(i)
        return result

    def func(text):
        alphabet = 'абвгдеёжзийклмнопрстуфхчшщъыьэюя'     
        reversed_alphabet = alphabet[::-1]
        atbash_dict = dict(zip(alphabet, reversed_alphabet))
        result = ''.join(atbash_dict.get(char, char) for char in text)
        return result

    def funcC(text):
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧШЩЪЫЬЭЮЯ'    
        reversed_alphabet = alphabet[::-1]
        atbash_dict = dict(zip(alphabet, reversed_alphabet))
        result = ''.join(atbash_dict.get(char, char) for char in text)
        return result
