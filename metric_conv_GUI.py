# pip install pysimplegui
# pip3 install pysimplegui
import PySimpleGUI as sg

sg.theme('TealMono')

layout = [
    [sg.Text('Data:'), sg.InputText(key='-IN-', size=(20, 1)),
     sg.Combo(('m', 'mm', 'cm', 'mi', 'in', 'ft', 'yd'), 'm', readonly=True,
     key='-IN-M-')],
    [sg.Text('Output:'), sg.Text('0', key='-OUT-', size=(16, 1)),
     sg.Combo(('m', 'mm', 'cm', 'mi', 'in', 'ft', 'yd'), 'm', readonly=True,
     key='-OUT-M-'), sg.Submit('Convert')]
]

window = sg.Window('Metric Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert' and values['-IN-'] != '':
        print(values)
window.close()
