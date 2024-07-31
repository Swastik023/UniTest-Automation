import matplotlib.pyplot as plt
import pandas as pd

def visualize_data(file_path):
    data = pd.read_csv(file_path)
    data.plot(kind='line', x='Load', y='Displacement')
    plt.title('UTM Data Visualization')
    plt.xlabel('Load')
    plt.ylabel('Displacement')
    plt.savefig('reports/utm_data_visualization.png')
    plt.show()

if __name__ == "__main__":
    data_path = 'data/processed_data/processed_utm_data.csv'
    visualize_data(data_path)
