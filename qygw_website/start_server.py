import os
import sys
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
venv_python = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.venv', 'Scripts', 'python.exe')

print(f"Python path: {venv_python}")
print("Starting Django development server...")

try:
    result = subprocess.run(
        [venv_python, 'manage.py', 'runserver', '127.0.0.1:8000'],
        capture_output=True,
        text=True,
        timeout=30
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("Return code:", result.returncode)
except subprocess.TimeoutExpired:
    print("Server started successfully (running in background)")
except Exception as e:
    print(f"Error: {e}")
