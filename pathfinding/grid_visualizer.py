import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

class GridVisualizer():
    def __init__(self, grid, pathfinding_func=None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.pathfinding_func = pathfinding_func
        
        self.fig = plt.figure(figsize=(6, 7))
        self.fig.canvas.manager.set_window_title('Pathfinder')
        self.ax = self.fig.add_axes([0.1, 0.2, 0.8, 0.75])
        
        ax_reset = self.fig.add_axes([0.25, 0.05, 0.2, 0.075])
        ax_findpath = self.fig.add_axes([0.55, 0.05, 0.2, 0.075])
        
        self.btn_reset = Button(ax_reset, 'Reset')
        self.btn_findpath = Button(ax_findpath, 'Find Path')
        
        self.btn_reset.on_clicked(self.reset)
        self.btn_findpath.on_clicked(self.find_path)
        
        self.fig.canvas.mpl_connect('button_press_event', self.on_grid_click)
        
        self.draw()
        
    def draw(self):
        self.ax.clear()
        
        grid_array = np.array(self.grid, dtype=float)
        
        self.ax.imshow(grid_array, cmap='gray_r', vmin=0, vmax=1, 
                      interpolation='nearest')
        
        self.ax.set_xticks(np.arange(-0.5, self.cols, 1), minor=True)
        self.ax.set_yticks(np.arange(-0.5, self.rows, 1), minor=True)
        self.ax.grid(which='minor', color='gray', linestyle='-', linewidth=1)
        
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        plt.draw()
        
    def on_grid_click(self, event):
        if event.inaxes != self.ax:
            return
            
        col = int(round(event.xdata))
        row = int(round(event.ydata))
        is_start_cell = row == col == 0
        is_target_cell = row == self.rows - 1 and col == self.cols - 1
        
        if 0 <= row < self.rows and 0 <= col < self.cols and not (is_start_cell or is_target_cell):
            self.grid[row][col] = not self.grid[row][col]
            self.draw()
    
    def mark_waypoints(self, waypoints):
        for i, (row, col) in enumerate(waypoints):
            self.ax.text(col, row, str(i), ha='center', va='center', color='green', fontsize=14, fontweight='bold')
        
        plt.draw()
        
    def reset(self, event):
        self.grid = [[False] * self.cols for _ in range(self.rows)]
        self.draw()
        
    def find_path(self, event):
        if self.pathfinding_func is None:
            return
            
        waypoints = self.pathfinding_func(self.grid)
        self.draw()
        self.mark_waypoints(waypoints)
        
    def show(self):
        plt.show()
