import tkinter as tk
import random
import string
from PIL import ImageTk, Image

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("600x400")  # Set the window size

# Load and display the background image
background_image_path = "image.jpg"  # Replace with the path to your background image
background_image = Image.open("python\image.jpg")
background_image = background_image.resize((600, 400))  # Resize the background image
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label( image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label and entry for the password length
length_label = tk.Label(window, text="Password Length:", font=("Comic Sans MS", 15, "bold"), fg="black")
length_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
length_entry = tk.Entry(window, font=("Comic Sans MS", 15, "bold"),justify='center')
length_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password",bg="#50aff2" ,command=generate_password, font=("Comic Sans MS", 12, "bold"))
generate_button.place(relx=0.5, rely=0.59, anchor=tk.CENTER)

# Create a label and entry to display the generated password

password_entry = tk.Entry(window, font=("Comic Sans MS", 15, "bold"),justify='center')
password_entry.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


# Start the GUI event loop
window.mainloop()
