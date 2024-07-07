import matplotlib.pyplot as plt
import pandas as pd

def get_data(path:str):
    labels = []
    values = []
    marvel_data = pd.read_csv(path, usecols=['movie', 'gross_world'])
    data_dict = marvel_data.to_dict(orient='records')
    for e in data_dict:
        labels.append(e["movie"])
        values.append(int(e["gross_world"]))
    return labels, values

def generate_graph(labels, values):
    # Create a horizontal bar graph
    plt.figure(figsize=(10, 6))
    plt.barh(labels, values, color='skyblue')
    plt.xlabel('Gross World Income (Billions)')
    plt.ylabel('Movies')
    plt.title('Marvel Movies World Gross Income')
    plt.grid(True)

    plt.subplots_adjust(left=0.2)  # Increase the left margin

    # Open the figure in fullscreen mode
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

    #Display the graph
    plt.show()
    return

if __name__ == "__main__":
    labels, values = get_data("data/mcu_films.csv")
    generate_graph(labels, values)
    