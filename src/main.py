import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# src/main.py
from src.graphConstructor import GraphConstructor

def main():
    # Sua lógica principal
    print(f"Projeto rodando...")
    GraphConstructor()
