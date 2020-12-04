# python-opencv-course
"Python for Computer Vision with OpenCV and Deep Learning" 2020 Udemy course by Jose Portilla.

These are my course notes and comments. I do not own syllabus, material or resources in this repository.

## Setup

1. Install Anaconda [docs](https://docs.anaconda.com/anaconda/install/) and reload the terminal or, in current terminal execute:
```
$ source ~/.bashrc
```
2. In Terminal, go to the root directory of this repository and execute:
```
$ conda env create -f cvcourse_linux.yml
$ conda activate python-cvcourse
$ jupyter-lab
```
3. This should automatically open a new tab in your default browser and load Jupyter Lab index page for the current project (at address `http://localhost:8888/lab`)

## Useful JupyterLab keyboard shortcuts

SHIFT + TAB = open Python documentation about function (when mouse hovers the function)
SHIFT + ENTER = execute current cell (`[*]` next to cell means that it is currently executing)

## Troubleshooting

If for some reason cell remains indefinitely in executing state (`[*]`) we need to restart the kernel.