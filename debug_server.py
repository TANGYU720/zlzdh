import os
import sys
import traceback

os.chdir('d:/TRAE/TRAR_TEST/QYGW/qygw_website')
sys.path.insert(0, 'd:/TRAE/TRAR_TEST/QYGW/qygw_website')

print("Python version:", sys.version)
print("Working directory:", os.getcwd())
print("Python path:", sys.executable)

try:
    print("\nSetting Django settings...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qygw_website.settings')
    
    print("Importing Django...")
    import django
    
    print("Setting up Django...")
    django.setup()
    
    print("Django setup complete")
    
    from django.core.management import call_command
    print("\nStarting runserver...")
    call_command('runserver', '127.0.0.1:8000', '--noreload')
    
except Exception as e:
    print("\nError occurred:")
    print(f"Type: {type(e).__name__}")
    print(f"Message: {e}")
    print("\nTraceback:")
    traceback.print_exc()