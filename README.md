# IITP Student Interpolation Project  

## Installation & Setup

### Clone the Repository  
```sh
git clone https://github.com/Nick18899/ittp.git
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


### Interpolation  
```sh
poetry run 
```

### Regular Grid  
```sh
poetry run regulargrid  
```
