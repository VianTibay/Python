class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id} | Name: {self.name} | Description: {self.description} | Price: ${self.price:.2f}"

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self):
        try:
            item_id = input("Enter Item ID: ").strip()
            if item_id in self.items:
                print("Error: Item ID already exists!")
                return

            name = input("Enter Item Name: ").strip()
            description = input("Enter Item Description: ").strip()
            price = float(input("Enter Item Price: "))
            if price < 0:
                raise ValueError("Price cannot be negative.")

            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

    def update_item(self):
        item_id = input("Enter Item ID to update: ").strip()
        if item_id not in self.items:
            print("Error: Item not found!")
            return
        
        try:
            name = input("Enter new name (leave blank to keep current): ").strip()
            description = input("Enter new description (leave blank to keep current): ").strip()
            price_input = input("Enter new price (leave blank to keep current): ").strip()
            
            if price_input:
                price = float(price_input)
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                self.items[item_id].price = price
            
            if name:
                self.items[item_id].name = name
            
            if description:
                self.items[item_id].description = description

            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_item(self):
        item_id = input("Enter Item ID to delete: ").strip()
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Error: Item not found!")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Create Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.create_item()
        elif choice == "2":
            manager.read_items()
        elif choice == "3":
            manager.update_item()
        elif choice == "4":
            manager.delete_item()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
