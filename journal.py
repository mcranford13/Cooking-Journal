import PySimpleGUI as sg
import os


'''
Possible addons:
Encryption
Entry History
Multiple
'''




'''
GUI Setup
'''
sg.change_look_and_feel("Dark")

gui_layout = [
         [sg.Text("", size=(20,1), key='date', justification='left'), 
         sg.In(key='cal', enable_events=True, visible=False), 
          sg.CalendarButton('Calendar', target="cal",
          font=('MS Sans Serif', 10, 'bold'),key='calendar', format=('%B, %d, %Y'))],
          [sg.Multiline(key='guiMulLine')],
        [sg.Submit(auto_size_button=True)]     
        ]

gui = sg.Window('Simple Journal', gui_layout, size=(300, 300))

cal_error_layout = [

        [sg.Text("", size=(20,2), key='error', justification='center')],
        [sg.Ok()]

]
entry_error_layout = [

        [sg.Text("", size=(20,2), key='error', justification='center')],
        [sg.Ok()]

]

# Functions
def SaveEntry(date,entry):

    #Check if file already exists?

    f = open(f"entries/{date}.jl", 'w', encoding='utf-8')
    
    f.write(f"{date}\n")
    f.write("==================\n")
    f.write(entry)
    f.close()
    
def ErrorHandler(message, param):
    if param == "cal":
        error = sg.Window("", cal_error_layout, size=(225,75), finalize=True)
    else:
        error = sg.Window("", entry_error_layout, size=(225,75), finalize=True)

    error["error"].update(f"Error!\n{message}")

    while True:
        event, values = error.read()
        if event in (None, 'Exit') or event in ("Ok"):
            break
    error.close()



def main():
    if not os.path.exists("entries"):
        os.mkdir("entries")

    while True:
        event, values = gui.read()
      
        if event in (None, 'Exit'):
            break
        if event in ("cal"):
            gui['date'].update(values["cal"])
        if event in ("Submit", "guiMulLine"):

            if values['cal'] == '':
                ErrorHandler("Date cannot be blank.", "cal")
            elif values['guiMulLine'] == '\n':
                ErrorHandler("Entry is blank!", "entry")
            else:
                selectedDate = values['cal']
                entryText = values["guiMulLine"]
            
                SaveEntry(selectedDate, entryText)
            
            
            

    gui.close() 



    return 0


main()


