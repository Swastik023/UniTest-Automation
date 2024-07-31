import subprocess
import time

def extract_data_from_utm():
    # Replace with actual command to interface with Universal Testing Machine
    subprocess.run(['echo', 'UTM data extraction command'])
    time.sleep(2)  # Simulate delay
    with open('data/raw_data/utm_data.csv', 'w') as file:
        file.write('Load,Displacement\n')
        for i in range(100, 1600, 50):
            file.write(f'{i},{i*0.002}\n')

def extract_data_from_uv_vis():
    # Replace with actual command to interface with UV-Vis spectrophotometer
    subprocess.run(['echo', 'UV-Vis data extraction command'])
    time.sleep(2)  # Simulate delay
    with open('data/raw_data/uv_vis_data.csv', 'w') as file:
        file.write('Wavelength,Absorbance\n')
        for i in range(300, 610, 10):
            file.write(f'{i},{i*0.001}\n')

if __name__ == "__main__":
    extract_data_from_utm()
    extract_data_from_uv_vis()
