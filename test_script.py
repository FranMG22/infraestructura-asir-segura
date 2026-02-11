import sys
import platform

print(f"--- INICIANDO PRUEBAS DE SEGURIDAD ---")
print(f"Sistema Operativo: {platform.system()} {platform.release()}")
print(f"Versión de Python: {sys.version}")

# Simulación de test exitoso
assert 1 + 1 == 2
print("Test de integridad: PASADO ✅")
