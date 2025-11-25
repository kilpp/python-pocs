"""Visualization functions for accessibility survey charts."""
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List, Optional, Tuple

from config import PlotConfig
from data_models import RespondentProfile, BarrierData, SupportData


class ChartGenerator:
    """Generate various types of charts for survey data."""
    
    def __init__(self, config: PlotConfig = PlotConfig()):
        """Initialize the chart generator with configuration."""
        self.config = config
    
    def _save_and_close(self, filepath: Path) -> None:
        """Save the current figure and close it."""
        plt.savefig(
            filepath, 
            dpi=self.config.DPI, 
            bbox_inches=self.config.BBOX_INCHES
        )
        print(f'Saved: {filepath}')
        plt.close()
    
    def create_pie_chart(
        self,
        labels: List[str],
        values: List[int],
        colors: List[str],
        title: str,
        filename: str,
        figsize: Tuple[int, int] = None,
        explode: Optional[Tuple[float, ...]] = None,
        start_angle: int = 140
    ) -> None:
        """
        Create a pie chart.
        
        Args:
            labels: Labels for each slice
            values: Values for each slice
            colors: Colors for each slice
            title: Chart title
            filename: Output filename
            figsize: Figure size (width, height)
            explode: Explode specific slices
            start_angle: Starting angle for the first slice
        """
        if figsize is None:
            figsize = self.config.PIE_CHART_SIZE
        
        plt.figure(figsize=figsize)
        plt.pie(
            values, 
            labels=labels, 
            autopct='%1.1f%%', 
            startangle=start_angle, 
            colors=colors,
            explode=explode
        )
        plt.title(title)
        plt.axis('equal')
        
        filepath = self.config.get_output_path(filename)
        self._save_and_close(filepath)
    
    def create_bar_chart(
        self,
        labels: List[str],
        values: List[int],
        color: str,
        title: str,
        filename: str,
        x_label: str = '',
        y_label: str = '',
        figsize: Tuple[int, int] = None,
        grid: bool = True
    ) -> None:
        """
        Create a bar chart.
        
        Args:
            labels: Labels for each bar
            values: Values for each bar
            color: Bar color
            title: Chart title
            filename: Output filename
            x_label: X-axis label
            y_label: Y-axis label
            figsize: Figure size (width, height)
            grid: Whether to show grid
        """
        if figsize is None:
            figsize = self.config.BAR_CHART_SIZE
        
        plt.figure(figsize=figsize)
        plt.bar(labels, values, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        
        if grid:
            plt.grid(axis='y', alpha=0.3)
        
        filepath = self.config.get_output_path(filename)
        self._save_and_close(filepath)
    
    def generate_respondent_profile_chart(
        self, 
        data: RespondentProfile
    ) -> None:
        """Generate respondent profile pie chart."""
        title = self.config.RESPONDENT_PROFILE_TITLE.format(total=data.total)
        self.create_pie_chart(
            labels=data.labels,
            values=data.values,
            colors=data.colors,
            title=title,
            filename=self.config.RESPONDENT_PROFILE_FILE
        )
    
    def generate_barriers_chart(self, data: BarrierData) -> None:
        """Generate barriers identification bar chart."""
        self.create_bar_chart(
            labels=data.labels,
            values=data.values,
            color=data.color,
            title=self.config.BARRIERS_TITLE,
            filename=self.config.BARRIERS_FILE,
            x_label=self.config.BARRIER_X_LABEL,
            y_label=self.config.BARRIER_Y_LABEL
        )
    
    def generate_support_chart(self, data: SupportData) -> None:
        """Generate project support consensus pie chart."""
        self.create_pie_chart(
            labels=data.labels,
            values=data.values,
            colors=data.colors,
            title=self.config.SUPPORT_TITLE,
            filename=self.config.SUPPORT_FILE,
            explode=data.explode,
            start_angle=90
        )
