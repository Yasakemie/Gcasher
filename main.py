import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os


# Function to generate fake GCash receipts and insert into the image
def generate_fake_gcash():
    # Replace this with your code for generating fake GCash receipts

    # Example generated data
    generated_name = "John Doe"
    generated_number = "123-456-7890"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Load the base image
    base_image_path = "images/gcash_profile.jpg"
    base_image = Image.open(base_image_path)

    # Load the font
    font_path = "fonts/Axiforma_Regular.ttf"
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)

    # Create a drawing context on the image
    draw = ImageDraw.Draw(base_image)

    # Calculate text size
    text = f"Name: {generated_name}\nNumber: {generated_number}\nTime: {current_time}"

    # Calculate the position to center the text
    image_width, image_height = base_image.size
    x = (image_width - 100) // 2
    y = (image_height - 100) // 2

    # Set the text color (you can adjust this as needed)
    text_color = (255, 255, 255)  # White color (RGB)

    # Insert the generated data into the image
    draw.text((x, y), text, font=font, fill=text_color)
    messagebox.showinfo("Select Area", "Click and drag to select the area on the image.")

    # Save or display the modified image (you can replace 'output.jpg' with your desired file path)
    base_image.save("output.jpg")

# Function to open and display the "gcash_profile.jpg" image
def open_gcash_profile():
    image_path = "images/gcash_profile.jpg"

    # Create a separate window for displaying the image
    image_window = tk.Toplevel(root)
    image_window.title("GCash Profile")

    # Open and resize the image to fit within the window dimensions
    image = Image.open(image_path)
    max_width, max_height = image_window.winfo_screenwidth() - 100, image_window.winfo_screenheight() - 100
    image.thumbnail((max_width, max_height))

    # Convert the image to a PhotoImage object for display
    img = ImageTk.PhotoImage(image)

    # Create a Label to display the image
    label = tk.Label(image_window, image=img)
    label.image = img
    label.pack()

# Function to open and edit the "name_dictionary" text file
def edit_name_dictionary():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        # Replace this with your code to open and edit the "name_dictionary" file
        print(f"Editing 'name_dictionary' file: {file_path}")


# Function to open and edit the "number_dictionary" text file
def edit_number_dictionary():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        # Replace this with your code to open and edit the "number_dictionary" file
        print(f"Editing 'number_dictionary' file: {file_path}")


# Create the main application window
root = tk.Tk()
root.title("Fake GCash Generator")

# Create a Notebook (tabs) for multiple sections
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')

# Tab 1: Generate Fake GCash Receipts
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Generate GCash Receipts')

# Create a Treeview widget with three columns in Tab 1
tree = ttk.Treeview(tab1, columns=("Generated Name", "Generated Number", "Time"), show="headings")

# Define column headings
tree.heading("Generated Name", text="Generated Name")
tree.heading("Generated Number", text="Generated Number")
tree.heading("Time", text="Time")

# Set column widths
tree.column("Generated Name", width=150)
tree.column("Generated Number", width=150)
tree.column("Time", width=150)

# Pack the Treeview widget
tree.pack()

# Button to generate fake GCash receipts
button1 = tk.Button(tab1, text="Generate Fake Receipts", command=generate_fake_gcash)
button1.pack()

# Button to open and edit the "name_dictionary" text file
button2 = tk.Button(tab1, text="Edit fake mobile names", command=edit_name_dictionary)
button2.pack()

# Button to open and edit the "number_dictionary" text file
button3 = tk.Button(tab1, text="Edit fake mobile numbers", command=edit_number_dictionary)
button3.pack()

# Tab 2: Open and Display "gcash_profile.jpg"
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Open GCash Profile')

# Dropdown menu to select and display the "gcash_profile.jpg" image
dropdown = ttk.Combobox(tab2, values=["gcash_profile.jpg"], state="readonly")
dropdown.set("Select Image")

# Button to open and display the selected image
button4 = tk.Button(tab2, text="Open Selected Image", command=open_gcash_profile)

# Arrange the components in Tab 2
dropdown.pack()
button4.pack()

# Start the Tkinter main loop
root.mainloop()
