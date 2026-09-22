people = [
    
    {"id": 1, "email": "vasya1234@mail"},
    {"id": 2,  "email": "sasha@mail"},
    {"id": 3, "email": "serega123@mail"}
]
def find_email(users, user_id):
    for person in users:
        if person["id"] == user_id:
            return person["email"]
    return "нет"

print(find_email(people, 1))
print(find_email(people, 999))