import mysql.connector
import mysql.connector.cursor


class StoreModel:
    def __init__(self) -> None:
        try:
            self.con = mysql.connector.connect(
                host="localhost", user="root", password="", database="flask_rest"
            )
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(
                f"Some error raise when mysql.connector try to connect with sql server {err}"
            )

    def get_full_store_details(self):
        try:
            self.cur.execute("SELECT * FROM store")
            result = self.cur.fetchall()
            if len(result) > 0:
                return self.cur.fetchall()
            else:
                return "Nothing to found!"
        except mysql.connector.Error as err:
            return {"Error": str(err)}

    def create_new_store(self, data):
        try:
            self.cur.execute(f"INSERT INTO store(name) VALUES('{data['name']}')")
            if self.cur.rowcount > 0:
                return "Store created successfully!"
            else:
                return "Operation failed!"
        except mysql.connector.Error as err:
            return {"Error": str(err)}

    def update_store(self, data, id):
        try:
            self.cur.execute(f"UPDATE store SET name='{data['name']}' WHERE id='{id}'")
            if self.cur.rowcount > 0:
                return "Store updated successfully!"
            else:
                return "Operation failed!"
        except mysql.connector.Error as err:
            return {"Error": str(err)}

    def delete_store(self, id):
        try:
            self.cur.execute(f"DELETE FROM store WHERE id='{id}'")
            if self.cur.rowcount > 0:
                return "Store deleted successfully!"
            else:
                return "Operation failed!"
        except mysql.connector.Error as err:
            return {"Error": str(err)}
