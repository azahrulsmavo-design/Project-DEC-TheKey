import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def generate_heatmap():
    # Ensure assets directory exists
    os.makedirs('assets', exist_ok=True)

    # Load data
    try:
        df = pd.read_csv('data/student_combined_data.csv')
    except FileNotFoundError:
        print("Error: data/student_combined_data.csv not found.")
        return

    # Select columns for correlation
    correlation_data = df[['performance_score', 'aptitude_score']]
    
    # Calculate correlation matrix
    corr = correlation_data.corr()

    # Create figure
    plt.figure(figsize=(8, 6))

    # Generate heatmap
    # Using 'Reds' colormap to match the user's request
    # annot=True to show values, fmt='.2g' for general number format (cleaner than .2f for 1)
    ax = sns.heatmap(
        corr, 
        annot=True, 
        cmap='Reds', 
        fmt='.2g', 
        linewidths=1, 
        linecolor='white',
        cbar_kws={"shrink": .8},
        square=True
    )

    # Set title
    plt.title('Correlation Heatmap: Performance vs Aptitude Score', pad=20)
    
    # Save figure
    output_path = 'assets/correlation_heatmap.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Heatmap saved to {output_path}")

    print("\n--- Correlation Within Each Course Level ---")
    levels = df['course_level'].unique()
    for level in levels:
        subset = df[df['course_level'] == level]
        r = subset['performance_score'].corr(subset['aptitude_score'])
        print(f"{level}: r = {r:.4f}")

if __name__ == "__main__":
    generate_heatmap()
