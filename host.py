import subprocess
import sys

PORT = 8000

if __name__ == "__main__":
    subprocess.call([sys.executable, "-m", "http.server", str(PORT)])
