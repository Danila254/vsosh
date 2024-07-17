class Atbash:
    def encrypt(text):
         alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧШЩЪЫЬЭЮЯ'
         alpha = 'абвгдеёжзийклмнопрстуфхчшщъыьэюя'
        
         for i in text:
             if i.islower():
                 text(alpha)
                 else:
                     text(alphabet)
