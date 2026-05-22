from grid_visualizer import GridVisualizer

class Maze():
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.target_cell = (self.rows - 1, self.cols - 1)
        
    def get_cell_value(self, cell):
        """
        True = Wall, False = Free
        """
        row = cell[0]
        col = cell[1]
        is_in_bounds = row >= 0 and col >= 0 and row < self.rows and col < self.cols
        
        if not is_in_bounds:
            return True

        return self.grid[row][col]
        
    def list_eligible_neighbors(self, cell, path):
        candidates = [
            (cell[0], cell[1] + 1),
            (cell[0] + 1, cell[1]),
            (cell[0], cell[1] - 1),
            (cell[0] - 1, cell[1])
        ]
        
        return [c for c in candidates if not self.get_cell_value(c) and not c in path]
    
    def is_solving_path(self, path):
        return not path is None and len(path) > 0 and path[-1] == self.target_cell
        
    def backtrack(self, cell=(0, 0), path=None):
        if path is None:
            path = []
        
        extended_path = [*path, cell]
        
        if self.is_solving_path(extended_path):
            # We reached the goal!
            return extended_path
        
        eligible_neighbors = self.list_eligible_neighbors(cell, path)
        
        for neighbor_cell in eligible_neighbors:
            backtracked_path = self.backtrack(neighbor_cell, extended_path)
            
            if self.is_solving_path(backtracked_path):
                return backtracked_path
            
        return None

def my_pathfinding(grid):
    maze = Maze(grid)
    path_through_maze = maze.backtrack()
    
    return path_through_maze

if __name__ == "__main__":
    rows = 10
    cols = 10
    my_grid = [[False] * cols for _ in range(rows)]
    viz = GridVisualizer(grid=my_grid, pathfinding_func=my_pathfinding)
    viz.show()