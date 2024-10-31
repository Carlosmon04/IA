import random
import string


numeros=string.digits
simbolos=string.punctuation
mayusculas=string.ascii_uppercase
minusculas=string.ascii_lowercase
password=random.sample(numeros,2) + random.sample(mayusculas,2) + random.sample(minusculas,2) + random.sample(simbolos,2)
final= random.sample(password,len(password))
print(''.join(final))




