from database import Database

class UserProfileManager:
    def __init__(self):
        self.db = Database.get_instance()

    def load_profile(self, email):
        query = "SELECT name, phone, gender, age, address FROM user_profiles WHERE email = %s"
        return self.db.fetch_one(query, (email,))

    def save_profile(self, data):
        # Check if profile exists
        check_query = "SELECT * FROM user_profiles WHERE email = %s"
        existing = self.db.fetch_one(check_query, (data['email'],))
        if existing:
            update_query = """
                UPDATE user_profiles
                SET name = %s, phone = %s, gender = %s, age = %s, address = %s
                WHERE email = %s
            """
            self.db.execute(update_query, (data['name'], data['phone'], data['gender'], data['age'], data['address'], data['email']))
        else:
            insert_query = """
                INSERT INTO user_profiles (email, name, phone, gender, age, address)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.db.execute(insert_query, (data['email'], data['name'], data['phone'], data['gender'], data['age'], data['address']))
