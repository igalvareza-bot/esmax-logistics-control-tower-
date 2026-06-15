# launcher_streamlit.py
# Lanzador para ejecutar main.py con Streamlit y abrir el navegador.
# Uso: python launcher_streamlit.py

import subprocess
import sys
import webbrowser
import time
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
MAIN = ROOT / "main.py"

if not MAIN.exists():
    print("Error: no se encontró main.py en la carpeta del proyecto.")
    sys.exit(1)

PORT = "8501"

cmd = [sys.executable, "-m", "streamlit", "run", str(MAIN), "--server.port", PORT]

log_file = ROOT / "streamlit_launcher.log"
with open(log_file, "ab") as lf:
    proc = subprocess.Popen(cmd, cwd=str(ROOT), stdout=lf, stderr=lf)

time.sleep(2)
try:
    webbrowser.open(f"http://localhost:{PORT}", new=2)
except Exception:
    pass

print(f"Streamlit iniciado (PID {proc.pid}). Abriendo http://localhost:{PORT}")
print(f"Logs: {log_file}")

try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    proc.wait()
    print("Streamlit detenido por usuario.")
