"""Configuration settings for the accessibility survey visualization."""
from pathlib import Path


class PlotConfig:
    """Configuration for plot generation."""
    
    # Output settings
    DPI = 300
    BBOX_INCHES = 'tight'
    OUTPUT_DIR = Path('.')
    
    # Figure sizes
    PIE_CHART_SIZE = (8, 6)
    BAR_CHART_SIZE = (10, 6)
    
    # Matplotlib backend
    BACKEND = 'Agg'
    
    # Chart titles
    RESPONDENT_PROFILE_TITLE = 'Perfil dos Respondentes (Total: {total})'
    BARRIERS_TITLE = 'Maior Dificuldade Encontrada (Infraestrutura)'
    SUPPORT_TITLE = 'Consenso: Apoio ao Projeto de Acessibilidade'
    
    # Chart labels
    BARRIER_X_LABEL = 'Barreira Citada'
    BARRIER_Y_LABEL = 'Número de Pessoas'
    
    # File names
    RESPONDENT_PROFILE_FILE = 'perfil_respondentes.png'
    BARRIERS_FILE = 'barreiras_identificadas.png'
    SUPPORT_FILE = 'consenso_apoio.png'
    
    @classmethod
    def get_output_path(cls, filename: str) -> Path:
        """Get full output path for a file."""
        return cls.OUTPUT_DIR / filename
