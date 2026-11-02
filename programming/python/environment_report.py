import platform
import sys


def generate_report():
    """Collect basic information about the current environment."""

    print("=" * 45)
    print("           DIGITAL LAB")
    print("          ENVIRONMENT REPORT")
    print("=" * 45)

    print(f"Operating System : {platform.system()}")
    print(f"OS Release       : {platform.release()}")
    print(f"Architecture     : {platform.machine()}")
    print(f"Python Version   : {platform.python_version()}")
    print(f"Python Impl.     : {platform.python_implementation()}")

    print("=" * 45)


if __name__ == "__main__":
    generate_report()
