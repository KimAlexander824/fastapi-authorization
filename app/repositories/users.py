# Захардкоженная бд вместо настоящей
# Пароль: 12345
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$p6YVpPzvxw9EvztzRtC71g$4QXsbX+/nfylsVIiIVEPNRrm4CXV+2kbDdcKFx7NaRs"
    }
}


def get_user_by_login(login: str) -> dict | None:
    return fake_users_db.get(login)
