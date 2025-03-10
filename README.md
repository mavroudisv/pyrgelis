# PyRgelis

A simulation of Rgelis floating in a surreal space. You can only win.

<img src="screenshot.png" style="width:600px;"/>

## Description

Far beyond the known realms of physics and reason, there exists a surreal, dreamlike world where the Rgelis drift eternally. These enigmatic, jellyfish-like beings float through the ethereal currents of their dimension, changing colors as they react to unseen cosmic forces.

Each Rgeli has a personality of its own, propelled by whimsical movements and ever-shifting hues. No one truly knows their purpose, but some say they are echoes of forgotten thoughts, living in an endless dance across the fabric of space.

## Installation

### Standard Installation

Install PyRgelis with pip:

```bash
pip install pyrgelis
```

This will automatically install the required dependencies (NumPy and Matplotlib).

### Development Installation

For development purposes, you can clone the repository and install from source:

```bash
git clone https://github.com/username/pyrgelis.git
cd pyrgelis
pip install -e .
```

### Troubleshooting Dependencies

If you encounter issues with dependencies:

1. Make sure you have the latest pip version:
   ```bash
   pip install --upgrade pip
   ```

2. You can manually install dependencies first:
   ```bash
   pip install numpy>=1.19.0 matplotlib>=3.3.0
   ```

3. On some systems, you might need additional libraries for Matplotlib to work correctly. For example, on Ubuntu:
   ```bash
   sudo apt-get install python3-tk
   ```

## Usage

### Command Line

After installation, you can run PyRgelis directly from the command line:

```bash
pyrgelis
```

#### Command Line Options

```
pyrgelis [-h] [--count COUNT] [--width WIDTH] [--height HEIGHT] 
         [--background BACKGROUND] [--no-welcome]
```

- `--count`, `-c`: Initial number of Rgelis (default: 5)
- `--width`, `-w`: Width of the space (default: 10)
- `--height`, `-H`: Height of the space (default: 10)
- `--background`, `-b`: Background color (default: black)
- `--no-welcome`: Skip the welcome message

### Controls

- **Mouse Click**: Create a new Rgeli at that position
- **Space Bar**: Pause/Resume the simulation
- **'c' Key**: Clear all Rgelis
- **'a' Key**: Add 5 random Rgelis

### As a Python Module

You can also use PyRgelis in your own Python projects:

```python
from pyrgelis import RgelisGame

# Create a game with 10 initial Rgelis
game = RgelisGame(num_rgelis=10)

# Run the simulation
game.run()
```

## Features

- Vibrant, colorful jellyfish-like creatures
- Emergent behavior through simple interaction rules
- Interactive summoning of new creatures
- Score tracking for interactions

## Advanced Usage

You can create your own custom Rgeli entities:

```python
from pyrgelis import Rgeli, RgelisGame
import numpy as np

# Create a custom Rgeli
custom_rgeli = Rgeli(
    x=5.0,  # X position
    y=5.0,  # Y position
    color='purple',  # Color
    size=100  # Size
)

# Create a game with custom settings
game = RgelisGame(
    num_rgelis=0,  # Start with no Rgelis
    width=15,  # Custom width
    height=15,  # Custom height
    background_color='darkblue'  # Custom background
)

# Add our custom Rgeli
game.rgelis.append(custom_rgeli)

# Add some random Rgelis too
for _ in range(5):
    game.spawn_random_rgeli()

# Run the simulation
game.run()
```

## Requirements

- Python 3.6+
- NumPy (>= 1.19.0)
- Matplotlib (>= 3.3.0)

These dependencies will be automatically installed when you install PyRgelis using pip.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the beauty of jellyfish and other bioluminescent creatures
- Created for those who appreciate the mesmerizing qualities of generative art
