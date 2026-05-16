import os
import subprocess
import requests  # More reliable than curl via os.system

def main():
    """Main function demonstrating safe network request."""
    try:
        # Example: Send a simple GET request (replace with your intended logic)
        response = requests.get("https://httpbin.org/get", timeout=5)
        print("Status Code:", response.status_code)
        print("Response:", response.json())
        
        # If you need to use curl via subprocess (safer than os.system)
        # subprocess.run(['curl', '-I', 'https://httpbin.org'], check=True)
        
    except requests.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
