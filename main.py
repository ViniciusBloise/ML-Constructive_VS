import tsplib_reader as tsplib
import time
from halo import Halo

if __name__ == '__main__':

    print('---------------------------------------------------')
    print('-- Generation of instances and optimal solutions --')
    print('---------------------------------------------------')

    spinner = Halo(text='Loading', spinner='dots')

    reader = tsplib.ReadTSPlib()

    for instance in reader.instances_generator():
        n_points, positions, distance_matrix, name, optimal_tour = instance

        spinner.start(text=name)

        #print(n_points, positions, distance_matrix, name, optimal_tour)
        time.sleep(1)

        spinner.succeed()
        #spinner.stop_and_persist()
        time.sleep(1)

    print('-- Finished generating graphs')