# Interface for simulation matrix plotting- Data in brief Article


This is a Python-based data visualization tool built using the Tkinter GUI library and Matplotlib for plotting. It allows users to select various parameters and plot data from text files. The tool is designed to work with specific file formats and output variable codes.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Select mesh type, fibre type, droplet material, failure mode, material model, blade position, and blade type.
- Choose output variables for both the x-axis and y-axis.
- Construct matrix variables based on user selections.
- Plot data from text files with gridlines.
- Automatic labeling of axes and title with variable names and units.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Required Python packages installed. You can install them using pip:

```bash
pip install matplotlib
```

## Installation

To install and run the application, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://gitlab.com/royson316/interface-for-simulation-matrix-plotting-data-in-brief-article.git
```

2. Change into the project directory:

```bash
cd interface-for-simulation-matrix-plotting-data-in-brief-article
```

3. Run the application:

```bash
python main.py
```

## Usage

Launch the application by running main.py.
Use the dropdown menus to select parameters and output variables.
Click the "Construct matrix variable and plot" button to generate and display the plot.
The plot will include gridlines, axis labels, and a title with variable names and units.

