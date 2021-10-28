import PySimpleGUI as sg


# def fahrenheit_to_celsius(fahrenheit):
#     """Convert the value for Fahrenheit to Celsius and insert the
#     result into lbl_result.
#     """
#     return (5/9) * (float(fahrenheit) - 32)


layout = [[sg.Input(size=10), sg.Button(
    "\N{RIGHTWARDS BLACK ARROW}"), sg.Text("\N{DEGREE FAHRENHEIT}")]]

window = sg.Window('Temperature Converter', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "\N{RIGHTWARDS BLACK ARROW}":
        # celsius = fahrenheit_to_celsius(values[0])
        celsius = (5/9) * (float(values[0]) - 32)
        layout[0][2].update(value=f"{round(celsius, 2)} \N{DEGREE CELSIUS}")

window.close()
