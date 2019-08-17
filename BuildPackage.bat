pyinstaller -F src\main.py
sphinx-apidoc -f -o .\docs .\src
sphinx-build -a .\docs .\html