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
    # sg.theme('DarkBlue14')

    total_votos, total_bozo, total_lula = 0, 0, 0

    # The window layout - defines the entire window
    layout = [[sg.Text('Vote no seu candidato')],
              [sg.Button('Bolsonaro', k="bozo")],
              [sg.Button('Lula', k="lula")],
              [sg.T(f'Total: {total_votos}', key="total_votos"),
               sg.T(f'Bolsonaro: {total_bozo}', k="total_bozo"),
               sg.T(f'Lula: {total_lula}', k="total_lula")],
              [sg.Radio('Normal', "modo", k="normal" ,default=True), 
               sg.Radio('3 x 1', "modo", k="3x1"), 
               sg.Radio('5 x 1', "modo", k="5x1")],
              [sg.Button('Reiniciar', k="reset")]]

    window = sg.Window("URNA FAKE", layout, size=(1024, 720),
                       location=(50, 50), finalize=True, element_justification="center", font="Calibri 18",
                       resizable=True, no_titlebar=False)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        # handle button clicks
        if values["normal"]:
            if event == 'bozo':
                total_bozo += 1
                total_votos = total_bozo + total_lula
                window["total_votos"].update(f'Total: {total_votos}')
                window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
                window["total_lula"].update(f'Lula: {total_lula}')
            elif event == 'lula':
                total_lula += 1
                total_votos = total_bozo + total_lula
                window["total_votos"].update(f'Total: {total_votos}')
                window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
                window["total_lula"].update(f'Lula: {total_lula}')
        elif values["3x1"]:
            if event == 'bozo':
                if (total_votos != 0 and total_votos % 2 == 1 and total_bozo % 3 == 0):
                    total_lula += 1
                    total_votos = total_bozo + total_lula
                    window["total_votos"].update(f'Total: {total_votos}')
                    window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
                    window["total_lula"].update(f'Lula: {total_lula}')
                else:
                    total_bozo += 1
                    total_votos = total_bozo + total_lula
                    window["total_votos"].update(f'Total: {total_votos}')
                    window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
                    window["total_lula"].update(f'Lula: {total_lula}')
            elif event == 'lula':
                total_lula += 1
                total_votos = total_bozo + total_lula
                window["total_votos"].update(f'Total: {total_votos}')
                window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
                window["total_lula"].update(f'Lula: {total_lula}')
        elif values["5x1"]:
            if event == 'bozo':
                if (total_votos != 0 and total_votos % 2 == 1 and total_bozo % 5 == 0):
                    total_lula += 1
                    total_votos = total_bozo + total_lula
                    window["total_votos"].update(f'Total: {total_votos}')
                    window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
                    window["total_lula"].update(f'Lula: {total_lula}')
                else:
                    total_bozo += 1
                    total_votos = total_bozo + total_lula
                    window["total_votos"].update(f'Total: {total_votos}')
                    window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
                    window["total_lula"].update(f'Lula: {total_lula}')
            elif event == 'lula':
                total_lula += 1
                total_votos = total_bozo + total_lula
                window["total_votos"].update(f'Total: {total_votos}')
                window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
                window["total_lula"].update(f'Lula: {total_lula}')  
        if event == "reset":
            total_votos, total_bozo, total_lula = 0, 0, 0
            window["total_votos"].update(f'Total: {total_votos}')
            window["total_bozo"].update(f'Bolsonaro: {total_bozo}')
            window["total_lula"].update(f'Lula: {total_lula}')  
        
    window.close()


if __name__ == '__main__':
    main()
