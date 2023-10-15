import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt

# Function to get the units of an output variable code
def get_variable_units(var_code):
    # Create a dictionary mapping output variable codes to their units
    variable_units = {
        "bd": "mm",
        "fd": "mm",
        "RF": "N",
        "ALLSE": "mJ",
        "ALLSE_i": "mJ",
        "ALLDMD": "mJ",
        "ALLIE": "mJ",
    }
    return variable_units.get(var_code, "")

# Function to get the full name of an output variable code
def get_variable_full_name(var_code):
    # Create a dictionary mapping output variable codes to their full names
    variable_full_names = {
        "bd": "Blade Displacement",
        "fd": "Fiber Displacement",
        "RF": "Reaction Force",
        "ALLSE": "Strain Energy",
        "ALLSE_i": "Interface Strain Energy",
        "ALLDMD": "Damage Energy",
        "ALLIE": "Internal Energy",
    }
    return variable_full_names.get(var_code, "")

# Function to construct the matrix variable and plot
def construct_variable():
    # Clear the previous plot
    plt.clf()

    # Mappings for variable construction
    mesh_mapping = {"Fine (f)": "f", "Coarse (c)": "c"}
    blade_position_mapping = {"P1": "A", "P2": "B", "P3": "C"}
    blade_type_mapping = {"Parallel (bp)": "bp", "Circular (bc)": "bc"}
    blade_position_type_mapping = {
        ("P1", "bp"): "A",
        ("P2", "bp"): "B",
        ("P3", "bp"): "C",
        ("P1", "bc"): "D",
        ("P2", "bc"): "E",
        ("P3", "bc"): "F"
    }

    combo_mapping = {
        ("Glass (GF)", "EP (EP)", "Mixed mode (L1)"): list(range(1, 5)),
        ("Glass (GF)", "EP (EP)", "Mode 1 (L2)"): list(range(5, 9)),
        ("Glass (GF)", "PPT (PPT)", "Mixed mode (L1)"): list(range(9, 13)),
        ("Glass (GF)", "PPT (PPT)", "Mode 1 (L2)"): list(range(13, 17)),
        ("Carbon (CF)", "EP (EP)", "Mixed mode (L1)"): list(range(17, 21)),
        ("Carbon (CF)", "EP (EP)", "Mode 1 (L2)"): list(range(21, 25)),
        ("Carbon (CF)", "PPT (PPT)", "Mixed mode (L1)"): list(range(25, 29)),
        ("Carbon (CF)", "PPT (PPT)", "Mode 1 (L2)"): list(range(29, 33)),
        ("Glass (GF)", "PP (PP)", "Mixed mode (L1)"): list(range(33, 37)),
        ("Glass (GF)", "PP (PP)", "Mode 1 (L2)"): list(range(37, 41)),
        ("Carbon (CF)", "PP (PP)", "Mixed mode (L1)"): list(range(41, 45)),
        ("Carbon (CF)", "PP (PP)", "Mode 1 (L2)"): list(range(45, 49))
    }

    # Construct variable based on user selections
    mesh_value = mesh_mapping.get(mesh_var.get())
    fibre_droplet_failure_combo = (fibre_var.get(), droplet_material_var.get(), failure_mode_var.get())
    model_value = combo_mapping.get(fibre_droplet_failure_combo, [])[int(material_model_var.get()[-1]) - 1]
    position_type_combo = blade_position_var.get() + "-" + blade_type_mapping.get(blade_type_var.get())
    position_type_value = blade_position_type_mapping.get((blade_position_var.get(), blade_type_mapping[blade_type_var.get()]))
    output_value = output_var.get()

    final_variable = f"{mesh_value}_{position_type_value}_{model_value}_{output_value}"
    output_label.config(text="Matrix variable: " + final_variable)

    # Construct the second matrix variable
    output2_value = output2_var.get()
    final_variable2 = f"{mesh_value}_{position_type_value}_{model_value}_{output2_value}"
    output_label.config(text="Matrix variable 1: " + final_variable + "\nMatrix variable 2: " + final_variable2)

    # Read data from .txt files and plot
    try:
        with open(f'./{final_variable}.txt', 'r') as file1, open(f'./{final_variable2}.txt', 'r') as file2:
            data1 = [float(line.strip()) for line in file1]
            data2 = [float(line.strip()) for line in file2]

            # Plotting
            plt.plot(data1, data2, '-o')
            # Add gridlines
            plt.grid(True)

            # Set axis labels
            plt.xlabel(final_variable)
            plt.ylabel(final_variable2)

            # Set the title with variable names and units
            var1_full_name = get_variable_full_name(output_var.get())
            var2_full_name = get_variable_full_name(output2_var.get())
            var1_units = get_variable_units(output_var.get())
            var2_units = get_variable_units(output2_var.get())
            plt.title(f"{var1_full_name} ({var1_units}) vs. {var2_full_name} ({var2_units})")

            plt.show()

    except FileNotFoundError:
        output_label.config(text="File not found for one of the variables.")

    return final_variable, final_variable2

# Create the main window
root = tk.Tk()
root.title("Select Parameters and Plot")

# Create labels and dropdowns for user selections

# Mesh type dropdown
tk.Label(root, text="Mesh Type").grid(row=0, column=0, padx=10, pady=5, sticky="w")
mesh_var = tk.StringVar(root)
mesh_dropdown = ttk.Combobox(root, textvariable=mesh_var, values=["Fine (f)", "Coarse (c)"])
mesh_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Fibre type dropdown
tk.Label(root, text="Fibre Type").grid(row=1, column=0, padx=10, pady=5, sticky="w")
fibre_var = tk.StringVar(root)
fibre_dropdown = ttk.Combobox(root, textvariable=fibre_var, values=["Glass (GF)", "Carbon (CF)"])
fibre_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Droplet material dropdown
tk.Label(root, text="Droplet Material").grid(row=2, column=0, padx=10, pady=5, sticky="w")
droplet_material_var = tk.StringVar(root)
droplet_material_dropdown = ttk.Combobox(root, textvariable=droplet_material_var, values=["EP (EP)", "PP (PP)", "PPT (PPT)"])
droplet_material_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Failure mode dropdown
tk.Label(root, text="Failure Mode").grid(row=3, column=0, padx=10, pady=5, sticky="w")
failure_mode_var = tk.StringVar(root)
failure_mode_dropdown = ttk.Combobox(root, textvariable=failure_mode_var, values=["Mixed mode (L1)", "Mode 1 (L2)"])
failure_mode_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Droplet material model dropdown
tk.Label(root, text="Droplet Material Model").grid(row=4, column=0, padx=10, pady=5, sticky="w")
material_model_var = tk.StringVar(root)
material_model_dropdown = ttk.Combobox(root, textvariable=material_model_var, values=["m1", "m2", "m3", "m4"])
material_model_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Blade position dropdown
tk.Label(root, text="Blade Position").grid(row=5, column=0, padx=10, pady=5, sticky="w")
blade_position_var = tk.StringVar(root)
blade_position_dropdown = ttk.Combobox(root, textvariable=blade_position_var, values=["P1", "P2", "P3"])
blade_position_dropdown.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

# Blade type dropdown
tk.Label(root, text="Blade Type").grid(row=6, column=0, padx=10, pady=5, sticky="w")
blade_type_var = tk.StringVar(root)
blade_type_dropdown = ttk.Combobox(root, textvariable=blade_type_var, values=["Parallel (bp)", "Circular (bc)"])
blade_type_dropdown.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

# Output type dropdown for x-axis
tk.Label(root, text="Output Type (x axis)").grid(row=7, column=0, padx=10, pady=5, sticky="w")
output_var = tk.StringVar(root)
output_dropdown = ttk.Combobox(root, textvariable=output_var, values=["bd", "RF", "fd", "ALLSE", "ALLSE_i", "ALLPD", "ALLDMD", "ALLIE"])
output_dropdown.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

# Output type dropdown for y-axis
tk.Label(root, text="Output Type (y axis)").grid(row=8, column=0, padx=10, pady=5, sticky="w")
output2_var = tk.StringVar(root)
output2_dropdown = ttk.Combobox(root, textvariable=output2_var, values=["bd", "RF", "fd", "ALLSE", "ALLSE_i", "ALLPD", "ALLDMD", "ALLIE"])
output2_dropdown.grid(row=8, column=1, padx=10, pady=5, sticky="ew")

# Output label to display the final matrix variable
output_label = tk.Label(root, text="Matrix variable: ", font=("Arial", 12))
output_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Button to construct the matrix variable and plot
construct_button = tk.Button(root, text="Construct matrix variable and plot", command=construct_variable)
construct_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()
