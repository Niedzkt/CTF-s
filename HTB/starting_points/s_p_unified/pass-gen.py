import crypt

# Hasło, które chcesz zhashować
password = "12345"

# Generowanie hasha w formacie SHA-512
salt = "$6$" + crypt.mksalt(crypt.METHOD_SHA512)  # Algorytm SHA-512
hashed_password = crypt.crypt(password, salt)

print("Hasło (x_shadow):", hashed_password)
