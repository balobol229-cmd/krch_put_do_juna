"""
Тренажёр bcrypt. FastAPI здесь нет — только пароль Васи.

Замок = hashpw + gensalt (регистрация).
Ключ в замок = checkpw (логин).
.encode = строка -> байты. .decode = байты-каша -> строка для БД.

Запусти из venv:
    source .venv/bin/activate
    python bcrypt_drill.py

Подставь код вместо None / .... Не копируй ответы из main.py глазами — напиши заново.
"""

import bcrypt

# --- Вася ---
vasya_plain = "qwerty"


# 1. Байты. bcrypt не ест обычную str.
# Одна строка: encode пароля Васи в utf-8.
vasya_bytes = vasya_plain.encode('utf-8')


# 2. Регистрация. Два аргумента у hashpw: байты пароля и gensalt().
# Результат — байты-каша. Пока НЕ decode.
vasya_hash_bytes =  bcrypt.hashpw(vasya_bytes, bcrypt.gensalt())


# 3. Колонка в SQLite у тебя String. Кашу в str.
# decode utf-8 от каши из задания 2.
vasya_hash_for_db = vasya_hash_bytes.decode('utf-8')


# 4. Логин правильным паролем. checkpw(байты_ввода, байты_каши).
# Каша в БД — строка. Снова encode. Не вызывай hashpw.
login_ok = bcrypt.checkpw(vasya_bytes, vasya_hash_bytes)


# 5. Петя ввёл "123456". Тот же замок Васи. Должно быть False.
petya_plain = "123456"
login_petya = bcrypt.checkpw(petya_plain.encode('utf-8'), vasya_hash_bytes)




# 6. Два раза hashpw одного пароля. Соль разная -> каши разные.
# Посчитай две каши (hashpw + gensalt) и сравни их через ==.
# В переменную запиши результат сравнения (это будет False).

bcrypt_hash_one = bcrypt.hashpw(vasya_bytes, bcrypt.gensalt())
bcrypt_has_two = bcrypt.hashpw(vasya_bytes, bcrypt.gensalt())

same_password_two_hashes_equal = bcrypt_hash_one == bcrypt_has_two




def run_checks() -> None:
    errors = []

    if not isinstance(vasya_bytes, bytes):
        errors.append("1: vasya_bytes должен быть bytes, не str и не None")
    elif vasya_bytes != vasya_plain.encode("utf-8"):
        errors.append("1: encode не от того пароля или не utf-8")

    if not isinstance(vasya_hash_bytes, bytes):
        errors.append("2: vasya_hash_bytes — байты от hashpw(..., gensalt())")
    elif not vasya_hash_bytes.startswith(b"$2"):
        errors.append("2: это не похоже на кашу bcrypt")

    if not isinstance(vasya_hash_for_db, str):
        errors.append("3: для БД нужна str после decode")
    elif isinstance(vasya_hash_bytes, bytes) and vasya_hash_for_db != vasya_hash_bytes.decode("utf-8"):
        errors.append("3: decode должен быть от той же каши, что в задании 2")

    if login_ok is not True:
        errors.append("4: правильный пароль Васи -> checkpw должен дать True")

    if login_petya is not False:
        errors.append("5: пароль Пети -> checkpw должен дать False")

    if same_password_two_hashes_equal is not False:
        errors.append("6: две каши одного пароля не равны. == должен быть False")

    if errors:
        print("Пока не ок:")
        for e in errors:
            print(" -", e)
        print("Допиши None / ... и запусти снова.")
        return

    print("Ок. Замок, ключ, байты, «две каши не равны» — это и есть bcrypt.")
    print("Дальше в проекте: GET без поля password, потом JWT.")


if __name__ == "__main__":
    run_checks()
