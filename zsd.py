arr1 = [chr(x) for x in range(65,91)]
arr2 = [x for x in arr1]
arr2.reverse()

text = ""

encrypt = ""
for i in text:
    for j,l in enumerate(arr1):
        if i==l:
            encrypt += arr2[j]
print(encrypt)

decrypt = " "
for i in encrypt:
    for j,l in enumerate(arr2):
        if i == l:
            decrypt += arr1[j]
print(decrypt)
