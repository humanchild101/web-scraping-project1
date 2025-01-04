"""
Author: Nikhila
Date Created: Jan 3, 2025
Description: A Python GUI application for selecting a website, entering an item description,
             choosing the number of results, and displaying scraped data from the selected website.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import web_scraping
def on_submit():
    submit_button.config(state=tk.DISABLED)
    selected_option = radio_var.get()
    text_input = entry_var.get()
    dropdown_value = dropdown_var.get()

    if not selected_option:
        messagebox.showwarning("Input Error", "Please select a website")
        submit_button.config(state=tk.NORMAL)
        return

    if not text_input:
        messagebox.showwarning("Input Error", "Please enter an item description")
        submit_button.config(state=tk.NORMAL)
        return

    if not text_input.strip() or dropdown_value == "Select an option":
        messagebox.showwarning("Input Error", "Please select number of results")
        submit_button.config(state=tk.NORMAL)
        return

    price_list = web_scraping.scrape(selected_option, text_input,dropdown_value)
    output_text = (
        f"Here is the items, price, and links:\n {price_list}"

    )
    output_area.config(state='normal')  # Make the output area editable temporarily
    output_area.delete(1.0, tk.END)  # Clear the output area
    output_area.insert(tk.END, output_text)  # Insert the new text
    output_area.config(state='disabled')  # Make the output area read-only again

    submit_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("Python GUI with Widgets")

# Radio buttons
radio_var = tk.StringVar(value="Option 1")
radio_label = tk.Label(root, text="Choose a website:")
radio_label.pack(anchor="w")
radio1 = tk.Radiobutton(root, text="deerdoll.com", variable=radio_var, value="deerdoll")
radio2 = tk.Radiobutton(root, text="petallush.com", variable=radio_var, value="petallush")
radio3 = tk.Radiobutton(root, text="cherieday.com", variable=radio_var, value="cherieday")
radio1.pack(anchor="w")
radio2.pack(anchor="w")
radio3.pack(anchor="w")

# Text input box
entry_var = tk.StringVar()
entry_label = tk.Label(root, text="Enter your desired item:")
entry_label.pack(anchor="w")
entry = tk.Entry(root, textvariable=entry_var)
entry.pack(fill="x")

# Dropdown menu
dropdown_var = tk.StringVar(value="Select an option")
dropdown_label = tk.Label(root, text="Choose number of results:")
dropdown_label.pack(anchor="w")
dropdown = ttk.Combobox(root, textvariable=dropdown_var)
dropdown['values'] = list(range(5, 25))
dropdown.pack(fill="x")

# Buttons frame
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

# Submit and Close buttons
submit_button = tk.Button(buttons_frame, text="Submit", command=on_submit)
submit_button.pack(side="left", padx=5)
close_button = tk.Button(buttons_frame, text="Close", command=root.destroy)
close_button.pack(side="left", padx=5)


# Output text area
output_label = tk.Label(root, text="Output:")
output_label.pack(anchor="w")
output_area = tk.Text(root, height=30, state='disabled')
output_area.pack(fill="both", expand=True)

# Start the Tkinter main loop
root.mainloop()
