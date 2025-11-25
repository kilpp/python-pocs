"""
Main application for generating accessibility survey visualizations.

This script generates three key visualizations:
1. Respondent profile distribution (pie chart)
2. Identified accessibility barriers (bar chart)
3. Project support consensus (pie chart)
"""
import matplotlib
from config import PlotConfig
from data_models import RespondentProfile, BarrierData, SupportData
from visualizations import ChartGenerator


def setup_matplotlib():
    """Configure matplotlib with appropriate backend."""
    matplotlib.use(PlotConfig.BACKEND)


def main():
    """Generate all accessibility survey visualizations."""
    # Setup
    setup_matplotlib()
    generator = ChartGenerator()
    
    # Load data (using default data for now)
    respondent_data = RespondentProfile.create_default()
    barrier_data = BarrierData.create_default()
    support_data = SupportData.create_default()
    
    # Generate visualizations
    print("Generating accessibility survey visualizations...")
    generator.generate_respondent_profile_chart(respondent_data)
    generator.generate_barriers_chart(barrier_data)
    generator.generate_support_chart(support_data)
    print("All visualizations generated successfully!")


if __name__ == '__main__':
    main()