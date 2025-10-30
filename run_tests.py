"""
Test runner script for the Mergington High School API tests.
This script can be used to run all tests with proper coverage reporting.
"""
import subprocess
import sys
import os

def run_tests():
    """Run all tests using pytest."""
    # Change to the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    # Run pytest with verbose output
    cmd = [
        sys.executable, "-m", "pytest", 
        "tests/", 
        "-v", 
        "--tb=short",
        "--color=yes"
    ]
    
    print("Running tests...")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 50)
    
    result = subprocess.run(cmd)
    return result.returncode

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)