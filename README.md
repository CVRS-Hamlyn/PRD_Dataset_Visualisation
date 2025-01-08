# PRD_Dataset_Visualisation
This is the python code to visualise the PRD Dataset available in [`Zenodo`](https://zenodo.org/records/7147878#.Y2jgNux_rn5).

## Environment Setup

1. Clone this repository and navigate to Git folder
```bash
git clone https://github.com/CVRS-Hamlyn/PRD_Dataset_Visualisation.git
cd PRD_Dataset_Visualisation
python -m venv env
source env/bin/activate
```

2. Install Package
```Shell
pip install -r requirements.txt
```

## Visualisation
In the `visualisation.py`, you can do:

- Visualize all .pkl files.
- Convert the concatenated .npy file to a video.

To run it:
```shell
python visualisation.py
```