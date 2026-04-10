#!/bin/bash
set -e  # przerwij przy błędzie

PROJECT_DIR="$(cd "$(dirname "$0")"; pwd)"
VENV_DIR="$PROJECT_DIR/.venv"
REQ_FILE="$PROJECT_DIR/updater/CONFIG/requirements.txt"

echo "PROJECT_DIR: $PROJECT_DIR"

# --- znajdź python ---
if command -v python3 >/dev/null 2>&1; then
    PYTHON_EXEC="python3"
else
    echo "Python3 nie znaleziony. Pobieranie portable..."
    curl -L -o python.tar.gz https://www.python.org/ftp/python/3.14.0/Python-3.14.0.tgz
    tar -xzf python.tar.gz -C "$PROJECT_DIR"
    PYTHON_EXEC="$PROJECT_DIR/python/bin/python3"
fi

# --- funkcja do stworzenia venv ---
create_venv() {
    echo "Tworzenie virtualenv..."
    rm -rf "$VENV_DIR"
    "$PYTHON_EXEC" -m venv "$VENV_DIR"
}

# --- jeśli brak venv → utwórz ---
if [ ! -d "$VENV_DIR" ]; then
    create_venv
fi

# --- aktywacja ---
source "$VENV_DIR/bin/activate"

# --- sprawdź czy pip działa ---
if ! command -v pip >/dev/null 2>&1; then
    echo "pip uszkodzony → rebuild venv"
    create_venv
    source "$VENV_DIR/bin/activate"
fi

echo "Aktualizacja pip..."
pip install --upgrade pip >/dev/null

echo "Instalacja zależności..."

# --- instalacja z retry (ważne przy update'ach) ---
if ! pip install --upgrade --no-cache-dir -r "$REQ_FILE"; then
    echo "Błąd instalacji → pełny reset venv"
    create_venv
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip
    pip install --no-cache-dir -r "$REQ_FILE"
fi

echo "Start aplikacji..."
python "$PROJECT_DIR/updater/PYTHON/__core__.py"