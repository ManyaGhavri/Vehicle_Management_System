import tkinter as tk
from tkinter import messagebox

# Vehicle Class (Base Class)
class Vehicle:
    def __init__(self, vehicle_id, brand, model, year):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"ID: {self.vehicle_id}, Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


# Car Class (Derived Class)
class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, num_doors):
        super().__init__(vehicle_id, brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return super().display_info() + f", Doors: {self.num_doors}"


# Truck Class (Derived Class)
class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, payload_capacity):
        super().__init__(vehicle_id, brand, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        return super().display_info() + f", Payload Capacity: {self.payload_capacity} tons"
# Motorcycle Class (Derived Class)
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, engine_displacement):
        super().__init__(vehicle_id, brand, model, year)
        self.engine_displacement = engine_displacement

    def display_info(self):
        return super().display_info() + f", Engine Displacement: {self.engine_displacement} cc"


# Vehicle Management System Class
class VehicleManagementSystem:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles.remove(vehicle)
                return True
        return False

    def get_all_vehicles(self):
        return [vehicle.display_info() for vehicle in self.vehicles]


# GUI Class
# Motorcycle Class (Derived Class)
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, engine_displacement):
        super().__init__(vehicle_id, brand, model, year)
        self.engine_displacement = engine_displacement

    def display_info(self):
        return super().display_info() + f", Engine Displacement: {self.engine_displacement} cc"

# Updating GUI Class to handle Motorcycles
class VehicleManagementApp:
    def __init__(self, root):
        self.vms = VehicleManagementSystem()
        self.root = root
        self.root.title("Vehicle Management System")

        # Labels and Entry fields
        tk.Label(root, text="Vehicle ID:").grid(row=0, column=0)
        self.entry_id = tk.Entry(root)
        self.entry_id.grid(row=0, column=1)

        tk.Label(root, text="Brand:").grid(row=1, column=0)
        self.entry_brand = tk.Entry(root)
        self.entry_brand.grid(row=1, column=1)

        tk.Label(root, text="Model:").grid(row=2, column=0)
        self.entry_model = tk.Entry(root)
        self.entry_model.grid(row=2, column=1)

        tk.Label(root, text="Year:").grid(row=3, column=0)
        self.entry_year = tk.Entry(root)
        self.entry_year.grid(row=3, column=1)

        tk.Label(root, text="Type (Car/Truck/Motorcycle):").grid(row=4, column=0)
        self.entry_type = tk.Entry(root)
        self.entry_type.grid(row=4, column=1)

        tk.Label(root, text="Additional Info (Doors/Payload/Engine cc):").grid(row=5, column=0)
        self.entry_info = tk.Entry(root)
        self.entry_info.grid(row=5, column=1)

        # Buttons
        tk.Button(root, text="Add Vehicle", command=self.add_vehicle).grid(row=6, column=0)
        tk.Button(root, text="Remove Vehicle", command=self.remove_vehicle).grid(row=6, column=1)
        tk.Button(root, text="Show All Vehicles", command=self.show_all_vehicles).grid(row=7, column=0, columnspan=2)

        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.grid(row=8, column=0, columnspan=2)

    def add_vehicle(self):
        vehicle_id = self.entry_id.get()
        brand = self.entry_brand.get()
        model = self.entry_model.get()
        year = self.entry_year.get()
        vehicle_type = self.entry_type.get().lower()
        additional_info = self.entry_info.get()

        if not (vehicle_id and brand and model and year and vehicle_type and additional_info):
            messagebox.showerror("Error", "All fields must be filled out")
            return

        try:
            year = int(year)
        except ValueError:
            messagebox.showerror("Error", "Year must be a number")
            return

        if vehicle_type == "car":
            try:
                num_doors = int(additional_info)
                vehicle = Car(vehicle_id, brand, model, year, num_doors)
            except ValueError:
                messagebox.showerror("Error", "Number of doors must be a number")
                return
        elif vehicle_type == "truck":
            try:
                payload_capacity = float(additional_info)
                vehicle = Truck(vehicle_id, brand, model, year, payload_capacity)
            except ValueError:
                messagebox.showerror("Error", "Payload capacity must be a number")
                return
        elif vehicle_type == "motorcycle":
            try:
                engine_displacement = int(additional_info)
                vehicle = Motorcycle(vehicle_id, brand, model, year, engine_displacement)
            except ValueError:
                messagebox.showerror("Error", "Engine displacement must be a number")
                return
        else:
            messagebox.showerror("Error", "Invalid vehicle type. Use 'Car', 'Truck', or 'Motorcycle'")
            return

        self.vms.add_vehicle(vehicle)
        messagebox.showinfo("Success", "Vehicle added successfully")
        self.clear_fields()

    def remove_vehicle(self):
        vehicle_id = self.entry_id.get()
        if not vehicle_id:
            messagebox.showerror("Error", "Vehicle ID is required")
            return

        if self.vms.remove_vehicle(vehicle_id):
            messagebox.showinfo("Success", "Vehicle removed successfully")
        else:
            messagebox.showerror("Error", "Vehicle ID not found")

        self.clear_fields()

    def show_all_vehicles(self):
        vehicles = self.vms.get_all_vehicles()
        self.text_area.delete(1.0, tk.END)
        if vehicles:
            for vehicle in vehicles:
                self.text_area.insert(tk.END, vehicle + "\n")
        else:
            self.text_area.insert(tk.END, "No vehicles available")

    def clear_fields(self):
        self.entry_id.delete(0, tk.END)
        self.entry_brand.delete(0, tk.END)
        self.entry_model.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)
        self.entry_type.delete(0, tk.END)
        self.entry_info.delete(0, tk.END)


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleManagementApp(root)
    root.mainloop()

