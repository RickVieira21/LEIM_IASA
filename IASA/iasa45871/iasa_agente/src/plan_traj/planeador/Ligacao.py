from dataclasses import dataclass

@dataclass
class Ligacao:
      origem: str
      destino: str
      custo: int