import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppVisitas


def main():

    root = tk.Tk()

    servicio = VisitaServicio()

    # INYECCIÓN DE DEPENDENCIA
    app = AppVisitas(root, servicio)

    root.mainloop()


if __name__ == "__main__":
    main()
