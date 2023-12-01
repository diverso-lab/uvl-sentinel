# UVL Sentinel (MODEVAR 24)

UVL Sentinel is a tool developed in Python that analyzes a massive dataset of feature models in UVL format, detects syntactic errors and applies common patterns to fix those models.

## Python environment

For simplicity, it is recommended to create a Python virtual environment to install the dependencies:

```
python -m venv env
```

### Activate (Windows)

```
env\Scripts\activate
```

### Activate (Linux/Mac)

```
source env/bin/activate
```

## Install

The whole process of ANTLR installation, installation of dependencies and other configuration can be done directly with this command:

```
make install
```

## Working with UVL Sentinel

### Generate analysis

To generate a model analysis, include your feature models with a .uvl extension inside the 'dataset' folder.

```
python main.py
```

### Generate summary

To obtain a summary of the above analysis, run the following:

```
python summary.py
```

### Fixing syntactic errors

To apply regular system-defined patterns to aid in syntax correction, run the following command. This will generate the new patterns in 'corrected_dataset'.

```
python fix.py
```