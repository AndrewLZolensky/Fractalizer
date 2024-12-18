import numpy as np

class FractalGenerator():
    def __init__(self, transforms, initial_points):
        self.transforms = transforms
        self.iterations = [initial_points]
    def build(self, k, history=False):
        self.iterations = [self.iterations[0]] # reset to initial point
        for _ in range(k):
            frontier = np.vstack([transform(self.iterations[-1]) for transform in self.transforms])
            if history or len(self.iterations) == 1:
                self.iterations.append(frontier)
            else:
                self.iterations[-1] = frontier
        return self.iterations[-1]

if __name__ == "__main__":
    
    import matplotlib.pyplot as plt
    
    # Define parameters
    angle = np.pi / 4  # Adjust angle for a visually interesting spiral
    scale = 0.7  # Scaling factor for each iteration
    center = np.array([0, 0])  # Central point
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle),  np.cos(angle/2)]])

    # Define transformations
    spiral_transforms = [
        lambda x: scale * ((x - center) @ rotation_matrix) + center + np.array([0.9, -0.3]),
        lambda x: scale * ((x - center) @ rotation_matrix.T) + center - np.array([-0.3, 0.3]),
        lambda x: scale * ((x - center) @ rotation_matrix) + center + np.array([-0.3, 0.4]),
        lambda x: scale * ((x - center) @ rotation_matrix) + center - np.array([0.3, -0.3]),
    ]

    # Create fractal generator
    engine = FractalGenerator(spiral_transforms, np.array([center]))

    # Generate fractal
    result = engine.build(8)  # Increase depth for better detail

    # Plot the fractal
    plt.figure(figsize=(4, 4))
    plt.axis("off")  # Remove axes for aesthetics
    cmap = plt.get_cmap("Blues")  # Choose a visually appealing colormap
    colors = cmap(np.linspace(0.5, 1, len(result)))  # Generate gradient colors
    plt.scatter(
        [point[0] for point in result],
        [point[1] for point in result],
        s=1,
        c=colors,
        edgecolor="none"
    )
    plt.show()