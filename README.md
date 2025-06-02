# ThreeBodySolution

ThreeBodySolution is a Python package that implements a symbolic shell classifier for predicting adaptive transitions in chaotic three body systems.
It identifies noetic contraction spikes in loss curves and field data, making it possible to forecast bifurcations before they happen.

## Installation

With a Python 3 interpreter activated:


## Usage

```python
from threebodysolution.classifier import ShellDetector

detector = ShellDetector()
result = detector.analyze(time_series_data)
print(result)
