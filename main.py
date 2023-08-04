from tkinter import *

windows = Tk()
windows.title("Mile to Km Converter")
windows.config(pady=20, padx=20)

miles_input = Entry(width=10)
miles_input.get()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_label = Label(text="is equal to")
km_label.grid(row=1, column=2)

calculated_km = Label(text=0)
calculated_km.grid(row=1, column=1)


def miles_converter():
    miles = float(miles_input.get())
    km = round(miles * 1.609344)
    calculated_km.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=miles_converter)
calculate_button.grid(row=2, column=1)

windows.mainloop()
