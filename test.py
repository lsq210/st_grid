from models import Sample, ST_GRID
import os

folder = 'E:/教学资料/科研/样本数据/合并/'
all_files = os.listdir(folder)
files = [x for x in all_files if '.csv' in x]
for file_name in files:
    ST_GRID.init()
    ST_GRID.load_samples(folder + file_name)
    ST_GRID.sovle_k_distance()
    # ST_GRID.print_samples()
    ST_GRID.plot_k_dist()
