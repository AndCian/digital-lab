import platform
import sys


def generate_report():
    """Collect basic information about the current environment."""
    print("=" * 50)
    print("                DIGITAL LAB")
    print("             ENVIRONMENT REPORT")
    print("=" * 50)
    print(f"Computer Name     : {platform.node()}")
    print(f"Operating System  : {platform.system()}")
    print(f"OS Release        : {platform.release()}")
    print(f"Processor         : {platform.processor() or 'Not detected'}")
    print(f"Architecture      : {platform.machine()}")
    print(f"Python Executable Arch. : {platform.architecture()[0]}")
    print("-" * 50)
    print(f"Python Version    : {platform.python_version()}")
    print(f"Python Impl.      : {platform.python_implementation()}")
    print(f"Python Executable : {sys.executable}")
    print("=" * 50)

if __name__ == "__main__":
    generate_report()
