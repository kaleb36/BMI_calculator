from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("BMI Calculator")
root.geometry("500x600")

def pass_command():
    pass

def clear_screen():
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.configure(text="")

def get_bmi_imperial():
    our_height = float(h_entry.get()) ** 2
    our_weight = int(w_entry.get())
    bmi1 = (our_weight / our_height) * 703
    bmi = round(bmi1, 1)

    if bmi < 18.5:
        results.configure(text=f"{bmi}\nUnderweight", text_color="blue")
    elif 18.5 <= bmi < 24.9:
        results.configure(text=f"{bmi}\nNormal", text_color="Green")
    elif 25 <= bmi <= 29.9:
        results.configure(text=f"{bmi}\nOverweight", text_color="#ffc87c")
    elif 30 <= bmi <= 34.9:
        results.configure(text=f"{bmi}\nObese", text_color="orange")
    elif 35 <= bmi <= 39.9:
        results.configure(text=f"{bmi}\nExtreme Obese", text_color="red")

def get_bmi_metric():
    #bmi = weight_kg / (height_m ** 2)
    our_height = float(h_entry.get())**2
    our_weight = int(w_entry.get())
    bmi = round(our_weight / our_height, 1)

    #results.configure(text=str(bmi))

    if bmi < 18.5:
        results.configure(text=f"{bmi}\nUnderweight", text_color="blue")
    elif 18.5 <= bmi < 24.9:
        results.configure(text=f"{bmi}\nNormal", text_color="Green")
    elif 25 <= bmi <= 29.9:
        results.configure(text=f"{bmi}\nOverweight", text_color="#ffc87c")
    elif 30 <= bmi <= 34.9:
        results.configure(text=f"{bmi}\nObese", text_color="orange")
    elif 35 <= bmi <= 39.9:
        results.configure(text=f"{bmi}\nExtreme Obese", text_color="red")

def segmented_button_callback(value):
    if value == "metric":
        h_entry.configure(placeholder_text="Height in meters")
        w_entry.configure(placeholder_text="Weight in kilograms")
        button_1.configure(command=get_bmi_metric)
    elif value == "imperial":
        h_entry.configure(placeholder_text="Height in inches")
        w_entry.configure(placeholder_text="Weight in pounds")
        button_1.configure(command=get_bmi_imperial)


meter = ImageTk.PhotoImage(Image.open("Untitled2.png"))
meter_img = Label(root, image=meter, bd=0)
meter_img.pack(pady=20)

segemented_button_var = customtkinter.StringVar(value="")
#start from here
segmented_button = customtkinter.CTkSegmentedButton(root, values=["metric", "imperial"],
                                                     command=segmented_button_callback,
                                                     variable=segemented_button_var)
segmented_button.pack(pady=10)

h_entry = customtkinter.CTkEntry(master=root, placeholder_text="",
                                 width=200, height=30,
                                 border_width=1, corner_radius=10)
h_entry.pack(pady=10)

w_entry = customtkinter.CTkEntry(master=root, placeholder_text="",
                                 width=200, height=30,
                                 border_width=1, corner_radius=10)
w_entry.pack(pady=20)

button_1 = customtkinter.CTkButton(master=root, text="calculate BMI",
                                   width=190, height=40, compound="top", command=pass_command)
button_1.pack(pady=20)

segmented_button_callback("metric")
segmented_button.set("metric")

button_2 = customtkinter.CTkButton(master=root, text="Clear Screen",
                                   width=190, height=40, fg_color="#D35B58", hover_color="#C77C78",
                                   command=clear_screen)
button_2.pack(pady=20)

results = customtkinter.CTkLabel(master=root, text="")
results.pack(pady=20)

root.mainloop()
