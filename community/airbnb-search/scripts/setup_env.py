import os
import sys
import subprocess

def run_command(command):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, text=True)
    if result.returncode != 0:
        print(f"Command failed with exit code: {result.returncode}")
        sys.exit(result.returncode)

def main():
    print("Setting up Airbnb Search Ability Dev Environment...")
    
    # Install python dependencies
    print("Installing Python dependencies...")
    run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Check gauge installation
    print("Verifying gauge installation...")
    try:
        subprocess.run(["gauge", "-v"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Gauge is installed.")
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Error: Gauge is not installed or not working correctly.")
        print("Please install gauge: https://docs.gauge.org/getting_started/installing-gauge.html")
        sys.exit(1)
        
    print("Setup complete. You can now run `just verify`.")

if __name__ == "__main__":
    main()
