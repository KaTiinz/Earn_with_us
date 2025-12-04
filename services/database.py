users = []

def save_user(tg_id, name):
    if not any(u["tg_id"] == tg_id for u in users):
        users.append({"tg_id": tg_id, "name": name})

def get_all_users():
    return users