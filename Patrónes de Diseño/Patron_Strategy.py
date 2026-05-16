from abc import ABC, abstractmethod

# 1. La interfaz Strategy
class EstrategiaExperiencia(ABC):
    @abstractmethod
    def calcular_exp(self, exp_base: int) -> int:
        pass

# 2. Estrategias Concretas
class PartidaNormal(EstrategiaExperiencia):
    def calcular_exp(self, exp_base: int) -> int:
        # La partida normal no da bonos adicionales
        return exp_base

class EventoEspecial(EstrategiaExperiencia):
    def calcular_exp(self, exp_base: int) -> int:
        # El evento multiplica la experiencia por 2
        return exp_base * 2

class PaqueteCompra(EstrategiaExperiencia):
    def calcular_exp(self, exp_base: int) -> int:
        # Los paquetes comprados dan un bono masivo (+5000 fijos)
        return exp_base + 5000

# 3. La clase Contexto
class Personaje:
    def __init__(self, nombre: str, estrategia: EstrategiaExperiencia):
        self.nombre = nombre
        self.estrategia = estrategia # Composición: el personaje "tiene" una estrategia

    def set_estrategia(self, nueva_estrategia: EstrategiaExperiencia):
        self.estrategia = nueva_estrategia

    def ganar_experiencia(self, exp_base: int):
        exp_final = self.estrategia.calcular_exp(exp_base)
        print(f"[{self.nombre}] ha ganado {exp_final} puntos de EXP.")

# --- Prueba del Escenario ---
if __name__ == "__main__":
    # Creamos un personaje con la estrategia por defecto
    jugador = Personaje("Guerrero Nvl 1", PartidaNormal())
    
    print("--- Jugando partida normal ---")
    jugador.ganar_experiencia(100)
    
    print("\n--- ¡Inicia el evento de fin de semana! ---")
    # Cambiamos la estrategia en tiempo de ejecución
    jugador.set_estrategia(EventoEspecial())
    jugador.ganar_experiencia(100)
    
    print("\n--- Reclamando paquete de nivel de personaje ---")
    # Cambiamos la estrategia nuevamente
    jugador.set_estrategia(PaqueteCompra())
    jugador.ganar_experiencia(100)