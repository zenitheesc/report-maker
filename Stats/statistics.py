import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium as fl
from time import sleep
import selenium.webdriver

# --------------------------------------------------------------------------------------------

# Generic function to generate line plot graphics of a dataType in function of the another dataType
# Examples: Temperature x Time; Pressure x Time

def generate_data_x_data (data, data2, dataType, dataType2):

    if pd.Series(data).is_unique == True:
        return -1                            

    else:
        df = pd.DataFrame(list(zip(data, data2)), columns= [f'{dataType}', f'{dataType2}'])
        
        # Set a graph design
        plt.style.use(u'seaborn-pastel')

        # Create graph
        plt.plot(df[f'{dataType2}'], df[f'{dataType}'], marker='', color='blue', linewidth=1, alpha=0.7)

        # Add titles
        plt.title(f"{dataType} x {dataType2}", loc='left', fontsize=12, fontweight=0, color='black')
        plt.xlabel(f'{dataType2}')
        plt.ylabel(f"{dataType}")

        # Save graph
        plt.savefig(f'graph_{dataType}_x_{dataType2}.png', dpi=96, bbox_inches='tight')
        plt.clf()
        return 1

# ----------------------------------------------------------------------------------------------

# Generic function to generate line plot graphics comparing 3 dataType, which are correlated through time
# Examples: Compare temp_int, temp_ext and temp_geral through time

def generate_compare_graph (data1, data2, data3, time, dataType1, dataType2, dataType3, comparing_data):

    df = pd.DataFrame(list(zip(data1, data2, data3, time)), columns= [f'{dataType1}', f'{dataType2}', f'{dataType3}', 'Time'])

    # Set a graph design
    plt.style.use(u'seaborn-pastel')

    # Create graph
    plt.plot(df['Time'], df[f'{dataType1}'], marker='', color='red', linewidth=1.5, alpha=0.7, label= f'{dataType1}')
    plt.plot(df['Time'], df[f'{dataType2}'], marker='', color='blue', linewidth=1.5, alpha=0.7, label= f'{dataType2}')
    plt.plot(df['Time'], df[f'{dataType3}'], marker='', color='green', linewidth=1.5, alpha=0.7, label= f'{dataType3}')

    # Add legend (Acertar)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

    # Add titles
    plt.title(f"Comparing {comparing_data}", loc='left', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Time (s)")                              # Podemos entrar como parâmetro as unidades de medida
    plt.ylabel(f"{comparing_data}")

    # Save graph
    plt.savefig(f'graph_compare_{comparing_data}.png', dpi=96, bbox_inches='tight')
    plt.clf()

# ----------------------------------------------------------------------------------------------

def generate_map (latitude, longitude):

    df = pd.DataFrame(list(zip(latitude, longitude)), columns= ['Latitude', 'Longitude'])

    # Create a map
    map = fl.Map(location=[-22.5254886, -45.8804367], tiles="OpenStreetMap", zoom_start=9)

    # Mark all coordinates
    for row in range(0,len(df)):
        fl.CircleMarker((df.loc[row, 'Latitude'], df.loc[row, 'Longitude']), radius=7, weight=5, color='red', fill_color='red', fill_opacity=.5).add_to(map)

    # Save the map as an html    
    map.save('Map.html')

    # Open a browser window to display the html file and screenshot the map

    driver = selenium.webdriver.PhantomJS()
    driver.set_window_size(4000, 3000) 
    driver.get('map.html')
    sleep(5)
    driver.save_screenshot('map.png')

# ----------------------------------------------------------------------------------------------
