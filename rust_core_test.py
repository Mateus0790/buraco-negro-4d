import math

class HyperBlackHole4D:
    def __init__(self, mass: float = 10.0):
        self.mass = float(mass)
        self.c = 299792458.0
        self.G_5 = 6.67430e-11 # Constante gravitacional 5D aproximada
        self.hbar = 1.054571817e-34
        self.k_B = 1.380649e-23
        self.D = 5 # Dimensões totais do espaço-tempo (4 espaciais + 1 temporal)

    def compute_event_horizon(self) -> float:
        """
        Calcula o raio do horizonte de eventos em 5D (Métrica de Schwarzschild-Tangherlini).
        r_h^2 = 8 * G_5 * M / (3 * pi * c^2)
        """
        if self.mass < 0:
            raise ValueError("A massa 4D não pode ser negativa!")
        if self.mass == 0:
            return 0.0
        
        # Fórmula física estrita baseada na especificação do sistema HiperSolar
        r_h_squared = (8.0 * self.G_5 * self.mass) / (3.0 * math.pi * (self.c ** 2))
        return math.sqrt(max(0.0, r_h_squared))

    def compute_hawking_temperature(self) -> float:
        """
        Temperatura de Hawking em 5D:
        T_H = (D - 3) * hbar * c / (4 * pi * k_B * r_h)
        com D = 5.
        """
        r_h = self.compute_event_horizon()
        if r_h == 0.0:
            return 0.0
        
        numerator = (self.D - 3) * self.hbar * self.c
        denominator = 4.0 * math.pi * self.k_B * r_h
        return numerator / denominator
