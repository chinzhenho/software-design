from database import Database

class MaterialAction:
    def execute(self, name, price):
        raise NotImplementedError("Subclasses must implement execute()")

class AddMaterial:
    def execute(self, material_name, price, center_name):
        db = Database.get_instance()
        query = "INSERT INTO materials (material_name, price, center_name) VALUES (%s, %s, %s)"
        params = (material_name, price, center_name)
        db.execute(query, params)

class UpdateMaterial:
    def execute(self, material_name, price, center_name):
        db = Database.get_instance()
        query = "UPDATE materials SET price = %s WHERE material_name = %s AND center_name = %s"
        params = (price, material_name, center_name)
        db.execute(query, params)

class MaterialActionFactory:
    @staticmethod
    def get_action(action_type):
        if action_type == "add":
            return AddMaterial()
        elif action_type == "update":
            return UpdateMaterial()
        else:
            raise ValueError("Invalid material action type.")
        
class MaterialReceptionHandler:
    def __init__(self):
        self.db = Database.get_instance()

    def update_received_material(self, center_name, material_name, amount_kg):
        query = """
            INSERT INTO recycle_center_materials (center_name, material_name, amount_kg)
            VALUES (%s, %s, %s)
        """
        self.db.execute(query, (center_name, material_name, amount_kg))