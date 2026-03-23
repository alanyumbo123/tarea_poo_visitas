import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class AppVisitas:

    def __init__(self, root, servicio):

        self.root = root
        self.root.title("Registro de Visitantes")

        # INYECCIÓN DE DEPENDENCIA
        self.servicio = servicio

        # ===== FORMULARIO =====
        tk.Label(root, text="Cédula").grid(row=0, column=0)
        self.cedula_entry = tk.Entry(root)
        self.cedula_entry.grid(row=0, column=1)

        tk.Label(root, text="Nombre").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1)

        tk.Label(root, text="Motivo").grid(row=2, column=0)
        self.motivo_entry = tk.Entry(root)
        self.motivo_entry.grid(row=2, column=1)

        # ===== BOTONES =====
        tk.Button(root, text="Registrar", command=self.registrar).grid(row=3, column=0)
        tk.Button(root, text="Eliminar", command=self.eliminar).grid(row=3, column=1)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=3, column=2)

        # ===== TABLA (Treeview) =====
        self.tabla = ttk.Treeview(root, columns=("cedula", "nombre", "motivo"), show="headings")

        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("motivo", text="Motivo")

        self.tabla.grid(row=4, column=0, columnspan=3)

    # ===== FUNCIONES =====

    def registrar(self):

        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        motivo = self.motivo_entry.get()

        if cedula == "" or nombre == "" or motivo == "":
            messagebox.showwarning("Error", "Campos vacíos")
            return

        ok = self.servicio.registrar_visitante(cedula, nombre, motivo)

        if ok:
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showwarning("Error", "Cédula ya existe")

    def eliminar(self):

        seleccionado = self.tabla.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        item = self.tabla.item(seleccionado)
        cedula = item["values"][0]

        self.servicio.eliminar_visitante(cedula)

        self.actualizar_tabla()

    def actualizar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for v in self.servicio.obtener_visitantes():
            self.tabla.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))

    def limpiar(self):

        self.cedula_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.motivo_entry.delete(0, tk.END)
