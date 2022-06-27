"""Aplication that helps to train the mind to do Scientific Remote Viewing."""

# Default imports

# External imports
import PySimpleGUI as sg

# Internal imports


def main():
    # Mensagem para versão console
    print("""Welcome!
Wait for the application to load!
Do not close this window!""")

    # THEME
    # Good Ones: DarkBlue14, Dark, DarkBlue, DarkBlue3, DarkTeal1, DarkTeal10, DarkTeal9, LightGreen
    sg.theme('DarkBlue14')

    # The tab 1, 2, 3 layouts - what goes inside the tab
    tab1_layout = [[sg.Text('Tab 1')],
                   [sg.Text('Put your layout in here')],
                   [sg.Text('Input something'), sg.Input(size=(12, 1), key='-IN-TAB1-')]]

    tab2_layout = [[sg.Text('Tab 2')]]
    tab3_layout = [[sg.Text('Tab 3')]]
    tab4_layout = [[sg.Text('Tab 4')]]

    # The TabgGroup layout - it must contain only Tabs
    tab_group_layout = [[sg.Tab('Tab 1', tab1_layout, key='-TAB1-'),
                        sg.Tab('Tab 2', tab2_layout,
                               visible=False, key='-TAB2-'),
                        sg.Tab('Tab 3', tab3_layout, key='-TAB3-'),
                        sg.Tab('Tab 4', tab4_layout,
                               visible=False, key='-TAB4-'),
                         ]]

    # The window layout - defines the entire window
    layout = [[sg.TabGroup(tab_group_layout,
                           enable_events=True,
                           key='-TABGROUP-')],
              [sg.Text('Make tab number'), sg.Input(key='-IN-', size=(3, 1)), sg.Button('Invisible'), sg.Button('Visible'), sg.Button('Select')]]

    window = sg.Window("SRV APP 0.1 - by Thiago Jung - thiagojm1984@hotmail.com", layout, size=(1024, 720),
                       location=(50, 50), finalize=True, element_justification="center", font="Calibri 18",
                       resizable=True, no_titlebar=False)

    # map from an input value to a key
    tab_keys = ('-TAB1-', '-TAB2-', '-TAB3-', '-TAB4-')
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        # handle button clicks
        if event == 'Invisible':
            window[tab_keys[int(values['-IN-'])-1]].update(visible=False)
        if event == 'Visible':
            window[tab_keys[int(values['-IN-'])-1]].update(visible=True)
        if event == 'Select':
            window[tab_keys[int(values['-IN-'])-1]].select()

    window.close()


if __name__ == '__main__':
    main()
