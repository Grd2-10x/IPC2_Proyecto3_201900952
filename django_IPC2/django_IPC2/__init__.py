# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#from Maquina import ListaMaq
#from Simulacion import ListaSimp
import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


def openFile():
    root = Tk()
    root.fileName = filedialog.askopenfilename(filetypes=(("HowCOde files", ".xml"), ("All files", ".")))
    file = root.fileName
    data = open(file, "r", encoding='utf8')
    aux = data.read()
    data.close()
    return aux


#Lista_Maquina = ListaMaq()
#Lista_Simulacion = ListaSimp()


class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("SmartUI.ui", self)
        self.Maquina.clicked.connect(self.CargaMaquina)
        self.Simulacion.clicked.connect(self.CargaSimulacion)
        self.pushButton.clicked.connect(self.Ayuda)
        self.BtnReportes.clicked.connect(self.Reporte)

    def CargaMaquina(self):
        print("cargando Maquina")
        cadena = openFile()

    def CargaSimulacion(self):
        print("cargando Simulacion")
        cadena = openFile()

    def Reporte(self):
        print("Generando Reporte")
        aux = 0
        dot = "digraph G { \n"
        dot += "L1C1 -> L2C1 -> L1C2\n"
        try:
            dot += "}"
            archivo = open("grafico.dot", 'w', encoding='utf8')
            archivo.write(dot)
            archivo.close()

            os.system("dot -Tpdf grafico.dot -o grafico.jpg")
        except Exception:

            return False
        contenido = ''
        htmFile = open("Reporte" + ".html", "w", encoding='utf8')
        htmFile.write("""<!DOCTYPE HTML PUBLIC"
                    <html>
                    <head>
                        <title>Reporte de tokens</title>
                     <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1">
                  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
                    </head>
                    <body>
                    <div class="container">
                  <h2>Reporte de tokens</h2>
                  <p>Lista de tokens</p>            
                  <table class="table">
                    <thead>
                      <tr>
                       <th>Fila</th>
                        <th>Columna</th>
                        <th>Token</th>
                        <th>Lexemna</th>
                      </tr>
                    </thead>
                    <tbody> 
                    </tbody>

                    """)

        htmFile.write(contenido)
        htmFile.write("""
                 </table>
            </div>
                </body>
                </html>""")
        htmFile.close

    def Ayuda(self):
        print("Datos Estudiante")
        messagebox.showinfo("DATOS ESTUDIANTE",
                            "GERARDO JOSE CIFUENTES LUNA" + "\n" + "201900952" + "\n" + 'Introduccion a la Programacion y Computacion 2 seccion "E" '
                            + "\n" + "Ingenieria en Ciencias y Sistemas" + "\n" + "5to Semestre")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec())


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
