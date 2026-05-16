class ConfiguracionWeb:
    _instancia = None # Variable de clase para almacenar la única instancia

    def __new__(cls):
        # Si la instancia no existe, la creamos. Si ya existe, retornamos la misma.
        if cls._instancia is None:
            print("Inicializando la configuración del club de programación por primera vez...")
            cls._instancia = super(ConfiguracionWeb, cls).__new__(cls)
            # Inicializamos variables de configuración
            cls._instancia.tema = "Modo Oscuro Minimalista"
            cls._instancia.base_datos = "Conectada"
        return cls._instancia

# --- Prueba del Escenario ---
if __name__ == "__main__":
    # Intentamos crear dos objetos diferentes
    config1 = ConfiguracionWeb()
    config2 = ConfiguracionWeb()

    print(f"Tema en config1: {config1.tema}")
    
    # Modificamos la configuración desde la segunda variable
    config2.tema = "Modo Claro"
    
    # Verificamos si el cambio afectó a la primera variable
    print(f"Tema en config1 después del cambio en config2: {config1.tema}")
    
    # Verificamos si ambas variables apuntan al mismo espacio en memoria
    print(f"¿config1 y config2 son el mismo objeto? {'Sí' if config1 is config2 else 'No'}")