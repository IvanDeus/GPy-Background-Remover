from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def remove_background():
    # Ask for input file
    input_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.webp;*.bmp"), ("All files", "*.*")]
    )
    
    if not input_path:
        return
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        # Create output path (same directory, original name + _nobg.png)
        output_path = input_path.rsplit('.', 1)[0] + '_nobg.png'
        output_image.save(output_path)
        # Show success message
        messagebox.showinfo("Success", f"Background removed successfully!\nSaved to: {output_path}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

# Create GUI
root = tk.Tk()
root.title("Background Remover")
root.geometry("300x100")

label = tk.Label(root, text="Select an image to remove background")
label.pack(pady=10)
process_btn = tk.Button(root, text="Select Image", command=remove_background)
process_btn.pack()
root.mainloop()
