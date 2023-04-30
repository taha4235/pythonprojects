# # # # # # # import tkinter as tk

# # # # # # # root = tk.Tk()

# # # # # # # # Create a scrollable frame
# # # # # # # canvas = tk.Canvas(root)
# # # # # # # scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# # # # # # # scrollable_frame = tk.Frame(canvas)

# # # # # # # scrollable_frame.bind(
# # # # # # #     "<Configure>",
# # # # # # #     lambda e: canvas.configure(
# # # # # # #         scrollregion=canvas.bbox("all")
# # # # # # #     )
# # # # # # # )

# # # # # # # canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# # # # # # # canvas.configure(yscrollcommand=scrollbar.set)

# # # # # # # # Add widgets to the scrollable frame
# # # # # # # for i in range(100):
# # # # # # #     tk.Label(scrollable_frame, text=f"Label {i}").pack()

# # # # # # # # Pack the scrollbar and canvas
# # # # # # # scrollbar.pack(side="right", fill="y")
# # # # # # # canvas.pack(side="left", fill="both", expand=True)

# # # # # # # root.mainloop()
# # # # # # import tkinter as tk

# # # # # # # Create the main window
# # # # # # root = tk.Tk()
# # # # # # root.geometry("300x300")

# # # # # # # Create a frame inside the window
# # # # # # frame = tk.Frame(root)
# # # # # # frame.pack(fill="both", expand=True)

# # # # # # # Create a scrollbar and attach it to the frame
# # # # # # scrollbar = tk.Scrollbar(frame)
# # # # # # scrollbar.pack(side="right", fill="y")

# # # # # # # Create a listbox inside the frame and attach it to the scrollbar
# # # # # # listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
# # # # # # for i in range(100):
# # # # # #     listbox.insert(tk.END, f"Item {i}")
# # # # # # listbox.pack(side="left", fill="both", expand=True)

# # # # # # # Configure the scrollbar to control the listbox
# # # # # # scrollbar.config(command=listbox.yview)

# # # # # # # # # Run the main loop
# # # # # # # # root.mainloop()
# # # # # # # import tkinter as tk
# # # # # # # import win32print

# # # # # # # def print_value():
# # # # # # #     # Get the default printer name
# # # # # # #     printer_name = win32print.GetDefaultPrinter()

# # # # # # #     # Create a printer handle
# # # # # # #     printer_handle = win32print.OpenPrinter(printer_name)

# # # # # # #     # Set the print job properties
# # # # # # #     job_info = {"DataType": "RAW", "DevMode": None, "pDocName": "PrintJob"}
# # # # # # #     job_id = win32print.StartDocPrinter(printer_handle, 1, job_info)
# # # # # # #     win32print.StartPagePrinter(printer_handle)

# # # # # # #     # Print the value
# # # # # # #     value = value_entry.get()
# # # # # # #     win32print.WritePrinter(printer_handle, value.encode())

# # # # # # #     # End the print job
# # # # # # #     win32print.EndPagePrinter(printer_handle)
# # # # # # #     win32print.EndDocPrinter(printer_handle)

# # # # # # # # Create the tkinter window
# # # # # # # window = tk.Tk()
# # # # # # # window.title("Print Value")

# # # # # # # # Create the value input field
# # # # # # # value_label = tk.Label(window, text="Enter value to print:")
# # # # # # # value_label.pack()
# # # # # # # value_entry = tk.Entry(window)
# # # # # # # value_entry.pack()

# # # # # # # # Create the print button
# # # # # # # print_button = tk.Button(window, text="Print", command=print_value)
# # # # # # # print_button.pack()

# # # # # # # # Start the tkinter event loop
# # # # # # # window.mainloop()
# # # # # # import tkinter as tk

# # # # # # root = tk.Tk()

# # # # # # entry = tk.Entry(root)
# # # # # # entry.pack()

# # # # # # def check_value():
# # # # # #     value = int(entry.get())
# # # # # #     if value > 0:
# # # # # #         print("The value is greater than 0.")
# # # # # #     else:
# # # # # #         print("The value is not greater than 0.")

# # # # # # button = tk.Button(root, text="Check Value", command=check_value)
# # # # # # button.pack()

# # # # # # root.mainloop()
# # # # # import tkinter as tk

# # # # # def set_scrollbar(frame):
# # # # #     canvas = tk.Canvas(frame, height=600)
# # # # #     scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
# # # # #     scrollable_frame = tk.Frame(canvas)

# # # # #     scrollable_frame.bind(
# # # # #         "<Configure>",
# # # # #         lambda e: canvas.configure(
# # # # #             scrollregion=canvas.bbox("all")
# # # # #         )
# # # # #     )

# # # # #     canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
# # # # #     canvas.configure(yscrollcommand=scrollbar.set)

# # # # #     # pack canvas and scrollbar
# # # # #     canvas.pack(side='left', fill='both', expand=True)
# # # # #     scrollbar.pack(side='right', fill='y')

# # # # #     # configure canvas scrollregion and bind mousewheel scrolling
# # # # #     canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1*(event.delta//120), "units"))

# # # # #     return scrollable_frame

# # # # # root = tk.Tk()

# # # # # # create a frame with some widgets inside
# # # # # main_frame = tk.Frame(root)
# # # # # tk.Label(main_frame, text="Some text").grid(row=0, column=0)
# # # # # for i in range(20):
# # # # #     tk.Button(main_frame, text=f"Button {i+1}").grid(row=i+1, column=0)

# # # # # # create a scrollable frame and add the main frame to it
# # # # # scrollable_frame = set_scrollbar(root)
# # # # # main_frame.pack(in_=scrollable_frame, fill='both', expand=True)

# # # # # # update scrollable frame size after packing
# # # # # root.update_idletasks()
# # # # # scrollable_frame.config(width=scrollable_frame.winfo_width(), height=scrollable_frame.winfo_height())

# # # # # # if frame height is less than 600, remove the scrollbar
# # # # # if scrollable_frame.winfo_height() < 600:
# # # # #     scrollable_frame.pack_forget()

# # # # # root.mainloop()
# # # # import tkinter as tk

# # # # def process_command():
# # # #     # Get command text from entry widget
# # # #     command_text = command_entry.get()
    
# # # #     # Process command and update output text
# # # #     output_text = "Command: {}\nOutput: {}".format(command_text, "Command processing not implemented yet.")
# # # #     output_label.config(text=output_text)

# # # # # Create main window
# # # # root = tk.Tk()
# # # # root.title("Command Line")

# # # # # Create entry widget for command input
# # # # command_entry = tk.Entry(root)
# # # # command_entry.grid(row=0, column=0, padx=5, pady=5)

# # # # # Create button to submit command
# # # # submit_button = tk.Button(root, text="Submit", command=process_command)
# # # # submit_button.grid(row=0, column=1, padx=5, pady=5)

# # # # # Create label widget to display output
# # # # output_label = tk.Label(root, text="Output will appear here.")
# # # # output_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# # # # # Start main event loop
# # # # root.mainloop()
import os
import subprocess
import tkinter as tk

class CommandWindow:
    def __init__(self, master):
  
        self.input_widget = tk.Entry(master,background="#222",fg="white")
        self.input_widget.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.input_widget.bind("<Return>", self.process_input)
        self.output_widget = tk.Text(master, state=tk.DISABLED,background="#222",fg="white")
        self.output_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
    
        self.cwd = os.getcwd()
    
        self.display_prompt()
    
    def process_input(self, event):
        # Get input text
        input_text = self.input_widget.get().strip()
        self.input_widget.delete(0, tk.END)
        
        # Exit if user enters "exit" or "quit"
        if input_text == "exit" or input_text == "quit":
            self.quit()
            return
        
        # Change directory if user enters "cd <directory>"
        if input_text.startswith("cd "):
            directory = input_text[3:]
            try:
                os.chdir(directory)
                self.cwd = os.getcwd()
                self.display_prompt()
            except FileNotFoundError:
                self.display_output("Directory not found: {}\n".format(directory))
            return
        
        # Run command and display output
        self.display_output("{}\n".format(self.format_command(input_text)))
        self.display_output("{}\n".format(self.run_command(input_text)))
        self.display_output("\n")
        self.display_prompt()
    
    def format_command(self, command):
        # Replace tilde with home directory
        return command.replace("~", os.path.expanduser("~"))
    
    def run_command(self, command):
        # Run command and return output
        try:
            output = subprocess.check_output(command, shell=True, cwd=self.cwd, stderr=subprocess.STDOUT)
            return output.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return e.output.decode("utf-8")
    
    def display_prompt(self):
        self.display_output("{} $ ".format(self.cwd), prompt=True)
    
    def display_output(self, text, prompt=False):
        # Enable text widget editing and insert text
        self.output_widget.config(state=tk.NORMAL)
        self.output_widget.insert(tk.END, text)
        
        # Disable text widget editing
        self.output_widget.config(state=tk.DISABLED)
        
        # Scroll to end of text widget
        self.output_widget.see(tk.END)
        
        # Display prompt if necessary
        if prompt:
            self.input_widget.focus_set()
    
    def quit(self):
        # Quit the application
        self.output_widget.destroy()
        self.input_widget.destroy()
        self.output_widget.quit()
        self.input_widget.quit()

# Create main window
root = tk.Tk()
root.iconbitmap("taha.ico")
root.title("Command Line")


command_window = CommandWindow(root)
root.mainloop()
# # import tkinter as tk
# # import os

# # # create the main window
# # root = tk.Tk()

# # # set the title of the window
# # root.title("Print Sheet")

# # # create a label widget with instructions
# # instructions = tk.Label(root, text="Enter the path of the sheet you want to print:", font=("Arial", 12))
# # instructions.pack(pady=20)

# # # create an entry widget to input the sheet path
# # sheet_path = tk.Entry(root, width=50)
# # sheet_path.pack(pady=10)

# # # define a function to print the sheet
# # def print_sheet():
# #     os.startfile(sheet_path.get(), "print")

# # # create a button widget to print the sheet
# # print_button = tk.Button(root, text="Print", command=print_sheet)
# # print_button.pack(pady=10)

# # # run the main event loop
# # root.mainloop()
# import tkinter as tk
# import os

# # create the main window
# root = tk.Tk()

# # set the title of the window
# root.title("Command Prompt")

# # create a label widget with instructions
# instructions = tk.Label(root, text="Enter a command:", font=("Arial", 12))
# instructions.pack(pady=20)

# # create an entry widget to input the command
# command_entry = tk.Entry(root, width=50)
# command_entry.pack(pady=10)

# # define functions for the commands
# def list_directory():
#     output.insert(tk.END, os.listdir())

# def remove_directory():
#     directory = command_entry.get()[6:]
#     os.rmdir(directory)
#     output.insert(tk.END, f"Removed directory: {directory}\n")

# def make_directory():
#     directory = command_entry.get()[6:]
#     os.mkdir(directory)
#     output.insert(tk.END, f"Created directory: {directory}\n")

# def show_help():
#     output.insert(tk.END, "Available commands:\n")
#     output.insert(tk.END, "ls - list contents of directory\n")
#     output.insert(tk.END, "rmdir <directory> - remove a directory\n")
#     output.insert(tk.END, "mkdir <directory> - create a directory\n")
#     output.insert(tk.END, "help - show available commands\n")

# # create a button widget to execute the command
# execute_button = tk.Button(root, text="Execute", command=lambda: execute_command(command_entry.get()))
# execute_button.pack(pady=10)

#  #create a text widget to display the output
# output = tk.Text(root, height=10, width=50)
# output.pack(pady=10)

# # define a function to execute the command
# def execute_command(command):
#     if command == "ls":
#         list_directory()
#     elif command.startswith("rmdir"):
#         remove_directory()
#     elif command.startswith("mkdir"):
#         make_directory()
#     elif command == "help":
#         show_help()
#     else:
#         output.insert(tk.END, "Command not recognized. Type 'help' to see available commands.\n")

# # run the main event loop
# root.mainloop()
# import tkinter as tk

# root = tk.Tk()

# text_widget = tk.Text(root, height=10)
# text_widget.pack(side="left", fill="both", expand=True)

# scrollbar = tk.Scrollbar(root, orient="vertical", command=text_widget.yview)
# scrollbar.pack(side="right", fill="y")

# text_widget.configure(yscrollcommand=scrollbar.set)

# root.mainloop()
