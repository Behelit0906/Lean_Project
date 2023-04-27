import tkinter as tk
import threading
from selenium import webdriver
from preparar_pagina.preparar_pagina import preparar_pagina
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

class MiApp:

    def __init__(self):
        # Crear ventana principal
        self.ventana = tk.Tk()

        # Configurar ventana
        self.ventana.title("Backlog")
        self.ventana.geometry("300x200")

        # Crear botones
        self.btn_iniciar = tk.Button(self.ventana, text="Iniciar", command=self.iniciar)
        self.btn_detener = tk.Button(self.ventana, text="Detener", command=self.detener, state=tk.DISABLED)

        # Ubicar botones en la ventana
        self.btn_iniciar.pack(pady=20)
        self.btn_detener.pack(pady=10)

        # Variable para controlar la ejecución de la operación
        self.ejecutando = False

    def iniciar(self):
        # Habilitar botón de detener
        self.btn_detener.config(state=tk.NORMAL)

        # Deshabilitar botón de iniciar
        self.btn_iniciar.config(state=tk.DISABLED)

        # Crear hilo para la función
        self.hilo = threading.Thread(target=self.ejecutar_funcion)

        # Iniciar hilo
        self.ejecutando = True
        self.hilo.start()

    def ejecutar_funcion(self):
        # Inicializar el navegador y abrir la página de Google
        self.driver = webdriver.Chrome()
        self.service = Service(r"C:\lean\edgedriver.exe")
        self.options = Options()
        self.download_dir = r"C:\lean\backlog_files"
        self.prefs = {"download.default_directory": self.download_dir}
        self.options.add_experimental_option("prefs", self.prefs)
        #self.options.add_argument('--headless=new')
        self.driver = webdriver.Edge(service=self.service, options=self.options)
        preparar_pagina(self.driver)


    def detener(self):
        # Detener la operación
        self.ejecutando = False
        self.driver.quit()

        # Actualizar etiqueta de estado
        self.etiqueta_estado.config(text="Operación detenida.")

        # Deshabilitar botón de detener
        self.btn_detener.config(state=tk.DISABLED)

        # Habilitar botón de iniciar
        self.btn_iniciar.config(state=tk.NORMAL)

    def run(self):
        # Crear etiqueta de estado
        self.etiqueta_estado = tk.Label(self.ventana, text="")
        self.etiqueta_estado.pack(pady=20)

        # Iniciar el bucle principal de la ventana
        self.ventana.mainloop()

# Crear instancia de la aplicación
app = MiApp()

# Iniciar aplicación
app.run()

