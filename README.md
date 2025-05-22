# IITP Student Interpolation Project  

## Installation & Setup

### Clone the Repository  
```sh
git https://github.com/Nick18899/ittp/tree/master
cd iitp_interpolation  
```

### Poetry Setup 
```sh
curl -sSL https://install.python-poetry.org | python3 - && poetry --version  
poetry config virtualenvs.in-project true  
poetry install  
```

## Linting & Code Formatting
Run Ruff to check and automatically fix issues:  
```sh
poetry run ruff check --fix  
```
Expected output:  
```sh
All checks passed!  
```

## Running the Project

### Cartesian Grid  
```sh
poetry run cartesiangrid --image_path [...] --limits [...] --points [...]  
```

### Interpolation  
```sh
poetry run interp  
```

### Regular Grid  
```sh
poetry run regulargrid  
```