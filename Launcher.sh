#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")"; pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

echo "PROJECT_DIR: $PROJECT_DIR"

if [ ! -d "$VENV_DIR" ]; then
    if ! command -v python3 >/dev/null 2>&1; then
        echo "Python3 nie jest zainstalowany. Pobieranie wersji portable..."
        curl -o python.tar.gz https://www.python.org/ftp/python/3.14.0/Python-3.14.0.tgz
        tar -xzf python.tar.gz -C "$PROJECT_DIR"
        PYTHON_EXEC="$PROJECT_DIR/python/bin/python3"
    else
        PYTHON_EXEC="python3"
    fi
    $PYTHON_EXEC -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip
    pip install -r "$PROJECT_DIR/updater/CONFIG/requirements.txt"
else
    source "$VENV_DIR/bin/activate"
fi

python "$PROJECT_DIR/updater/PYTHON/__core__.py"
