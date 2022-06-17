import time
from tsplib import readerTSP
from tsplib import plotterTSP
from halo import Halo

if __name__ == '__main__':

    print('---------------------------------------------------')
    print('-- Generation of instances and optimal solutions --')
    print('---------------------------------------------------')

    spinner = Halo(text='Loading', spinner='dots')

    reader = readerTSP.ReaderTSP()
    plotter = plotterTSP.PlotterTSP(None)

    fig = 1
    for instance in reader.instances_generator():
        n_points, positions, distance_matrix, name, optimal_tour = instance

        spinner.start(text=name)

        #print(n_points, positions, distance_matrix, name, optimal_tour)
        time.sleep(1)

        spinner.succeed()
        #spinner.stop_and_persist()
        #print(positions)

        plotter.set_figure(fig)
        plotter.plot_points(positions)
        plotter.show(False)
        fig += 1
        time.sleep(1)

    print('-- Finished generating graphs')
    plotter.show(True)
    time.sleep(5)