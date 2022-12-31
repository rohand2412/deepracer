import numpy as np
import re
import sys
import glob
import os
from typing import Tuple, Union
from shapely.geometry.polygon import LineString
import matplotlib.pyplot as plt
import matplotlib

#required for load_py_to_ndarray
from numpy import array

def list_available_tracks(track_path_npy: str = './tracks/') -> None:
    # Conveniently list available tracks to analyze
    available_track_files = glob.glob(os.path.join(track_path_npy, '**.npy'))
    available_track_names = list(map(lambda x: os.path.basename(x).split('.npy')[0], available_track_files))
    print(available_track_names)

def load_track_waypoints(track_name: str, track_path_npy: str = './tracks/') -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Load the center, inner, outer waypoints
    waypoints = np.load(os.path.join(track_path_npy, '%s.npy' % track_name))

    # Separate into center, inner, outer waypoints
    center_line = waypoints[:,0:2]
    inner_border = waypoints[:,2:4]
    outer_border = waypoints[:,4:6]

    return center_line, inner_border, outer_border

def plot_coords(ax: matplotlib.axes.Axes, ob: LineString, color: str = '#999999') -> None:
    x, y = ob.xy
    ax.plot(x, y, '.', color=color, zorder=1)

def plot_line(ax: matplotlib.axes.Axes, ob: LineString, color: str = 'cyan') -> None:
    x, y = ob.xy
    ax.plot(x, y, color=color, alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)

def print_border(ax: matplotlib.axes.Axes, inner_border: np.ndarray, outer_border: np.ndarray, color: str = 'gray', color_hex: str = '#646464') -> None:
    line = LineString(inner_border)
    plot_coords(ax, line, color_hex)
    plot_line(ax, line, color)

    line = LineString(outer_border)
    plot_coords(ax, line, color_hex)
    plot_line(ax, line, color)

def print_track(ax: matplotlib.axes.Axes, center_line: np.ndarray, inner_border: np.ndarray, outer_border: np.ndarray, color: str = 'cyan', color_hex: str = '#999999') -> None:
    line = LineString(center_line)
    plot_coords(ax, line, color_hex)
    plot_line(ax, line, color)

    print_border(ax, inner_border, outer_border, color, color_hex)

def new_figure(facecolor: str) -> matplotlib.figure.Figure:
    fig = plt.figure(1, figsize=(16, 10))
    fig.add_subplot(111, facecolor=facecolor)
    plt.axis('equal')
    return fig

def plot_track(center_line: np.ndarray, inner_border: np.ndarray, outer_border: np.ndarray, color: str = 'cyan', color_hex: str = '#999999') -> None:
    fig = new_figure('black')
    print_track(fig.gca(), center_line, inner_border, outer_border, color, color_hex)

def plot_border(inner_border: np.ndarray, outer_border: np.ndarray, color: str = 'gray', color_hex: str = '#646464') -> matplotlib.figure.Figure:
    fig = new_figure('white')
    print_border(fig.gca(), inner_border, outer_border, color, color_hex)
    return fig

def load_py_to_ndarray(py_path: str) -> np.ndarray:
    with open(py_path, "r") as file:
        deserialized = eval(file.read())
    return deserialized

def array2D_repr_columns(arr: np.ndarray, col: int, precision: int = 5) -> str:
    opt = np.get_printoptions()
    np.set_printoptions(precision=precision, suppress=True, threshold=sys.maxsize)
    arr_repr = np.array_repr(arr)
    np.set_printoptions(**opt)

    pattern = r'( *\[[^]]+\]),?\n?'
    for _ in range(col-1):
        pattern += r' *(\[[^]]+\]),?\n?'

    repl = r''
    for i in range(1, col + 1):
        repl += r'\g<{}>,'.format(i)
        repl += r'\t' if i != col else r'\n'

    return re.sub(pattern, repl, arr_repr)

def array1D_repr_columns(arr: np.ndarray, col: int, precision: int = 5) -> str:
    opt = np.get_printoptions()
    np.set_printoptions(precision=precision, suppress=True, threshold=sys.maxsize)
    arr_repr = np.array_repr(arr)
    np.set_printoptions(**opt)

    pattern = r''
    for _ in range(col):
        pattern += r'( *-?\d+\.[\d ]+),?\n? ?'

    repl = r''
    for i in range(1, col + 1):
        repl += rf'\g<{i}>, '
    repl += r'\n       '

    repr_cols = re.sub(r'\n      ', r'', arr_repr)
    return re.sub(pattern, repl, repr_cols)

def export_ndarray(arr: np.ndarray, prefix: str, ndarray_repr: str) -> None:
    py_fname = prefix + '.py'
    npy_fname = prefix + '.npy'
    with open(py_fname, "w") as file:
        print("Writing python code to %s" % py_fname)
        file.write(ndarray_repr)

    print("Writing numpy binary to %s" % npy_fname)
    np.save(npy_fname, arr)
