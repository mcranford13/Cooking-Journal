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

layout = [
         [sg.Text("", size=(20,1), key='date', justification='left'), 
         sg.In(key='cal', enable_events=True, visible=False), 
          sg.CalendarButton('Calendar', target="cal",
          font=('MS Sans Serif', 10, 'bold'),key='calendar', format=('%B, %d, %Y'))],
          [sg.Multiline(size=(30,12), key='guiMulLine')],
        [sg.Submit(auto_size_button=True)]     
        ]

gui = sg.Window('Simple Journal', layout, size=(300, 300))

# Functions
def SaveEntry(date,entry):

    #Check if file already exists?

    f = open(f"entries/{date}.jl", 'w', encoding='utf-8')
    
    f.write(f"{date}\n")
    f.write("==================\n")

    

    
    f.close()
    
   
def main():
    if not os.path.exists("entries"):
        os.mkdir("entries")

    while True:
        event, values = gui.read()
        print(event,values)
        if event in (None, 'Exit'):
            break
        if event in ("cal"):
            gui['date'].update(values["cal"])
        if event in ("Submit", "guiMulLine"):

            if values['cal'] == '':
                print("Please select a date to continue.")
            elif values['guiMulLine'] == '\n':
                print("Entry is blank!")
            else:
                selectedDate = values['cal']
                entryText = values["guiMulLine"]
            
                SaveEntry(selectedDate, entryText)
            

            

    gui.close() 



    return 0


main()


