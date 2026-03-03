## create sqlite database if not exist  
import sqlite3

def create_database(db_name):
    conn = sqlite3.connect(f'data/{db_name}')
    print(f"Database '{db_name}' created successfully.")
    conn.close()


## create table if not exist
def create_table(db_name, table_name, columns : dict):
    conn = sqlite3.connect(f'data/{db_name}')
    cursor = conn.cursor()
    

    columns = ", ".join([f"{col_name} {col_type} NOT NULL" for col_name, col_type in columns.items()])

    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            key INTEGER PRIMARY KEY AUTOINCREMENT,
            {columns}
        );
        """   

    cursor.execute(create_table_query)
    print(f"Table '{table_name}' created successfully.")
    
    conn.commit()
    conn.close()   


if __name__ == "__main__":
    db_name = "shoppingList.db"
    
    #create_database(db_name) 
    
    dishes = {
        "dish_id": "TEXT",
        "dish_name": "TEXT",
        "recipe": "TEXT",
        "tags": "TEXT"
    }
    
    create_table(db_name, "dishes", dishes)

    ingredients = {
        "ingredient_id": "TEXT",
        "ingredient_name": "TEXT",
        "quantity": "TEXT",
        "unit": "TEXT",
        "dish_id": "TEXT"
    }

    create_table(db_name, "ingredients", ingredients)





