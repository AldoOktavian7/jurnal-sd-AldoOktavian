import random

# Simulasikan data dari database
users = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "User"}
]

def get_users():
    angka = random.randint(1, 5)

    if angka == 3:
        return {
            "status": "error",
            "message": "Server sedang sibuk, coba lagi nanti."
        }

    return {
        "status": "success",
        "data": users
    }