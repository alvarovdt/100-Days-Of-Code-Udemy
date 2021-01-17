import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
entry_miles = tkinter.Entry(width=7)
entry_miles.grid(column=1, row=0)

label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text="is equal to")
label_equal.grid(column=0, row=2)
label_km = tkinter.Label(text="0")
label_km.grid(column=1, row=2)
label_km_txt = tkinter.Label(text="Km")
label_km_txt.grid(column=2, row=2)


def miles_to_km():
    value = round(float(entry_miles.get()) * 1.609, 2)
    label_km.config(text=f"{value}")


button_calculate = tkinter.Button(text="Calculate", command=miles_to_km)
button_calculate.grid(column=1, row=3)
window.mainloop()
