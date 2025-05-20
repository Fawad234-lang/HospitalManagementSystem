from app.models.user import User

users = [User("admin", "admin123")]

def authenticate_user(username, password):
    return any(user.username == username and user.password == password for user in users)

def register_user(username, password):
    if any(user.username == username for user in users):
        return False
    users.append(User(username, password))
    return True
