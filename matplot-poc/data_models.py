"""Data models for accessibility survey analysis."""
from dataclasses import dataclass
from typing import List


@dataclass
class SurveyData:
    """Base class for survey data."""
    labels: List[str]
    values: List[int]
    colors: List[str]


@dataclass
class RespondentProfile:
    """Data for respondent profile distribution."""
    labels: List[str]
    values: List[int]
    colors: List[str]
    total: int

    @classmethod
    def create_default(cls) -> 'RespondentProfile':
        """Create default respondent profile data."""
        return cls(
            labels=['Clientes (187)', 'Equipe/Fornecedores (25)'],
            values=[187, 25],
            colors=['#4CAF50', '#FFC107'],  # Verde e Amarelo
            total=212
        )


@dataclass
class BarrierData:
    """Data for identified accessibility barriers."""
    labels: List[str]
    values: List[int]
    color: str

    @classmethod
    def create_default(cls) -> 'BarrierData':
        """Create default barrier data."""
        return cls(
            labels=['Escadas/Falta de Rampa', 'Banheiro Inadequado', 
                   'Circulação Interna', 'Nenhuma'],
            values=[130, 50, 22, 10],
            color='#FF5722'
        )


@dataclass
class SupportData:
    """Data for project support consensus."""
    labels: List[str]
    values: List[int]
    colors: List[str]
    explode: tuple

    @classmethod
    def create_default(cls) -> 'SupportData':
        """Create default support data."""
        return cls(
            labels=['A Favor da Inclusão/Reforma', 'Satisfeitos com Atual'],
            values=[203, 9],  # 96% a favor
            colors=['#2196F3', '#FF0022'],  # Azul destaque e Vermelho
            explode=(0.1, 0)
        )
