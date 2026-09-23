import importlib

REQUIRED_PACKAGES = [
    "flask",
    "flask_cors",
    "cv2",
    "google.generativeai",
    "numpy",
    "requests",
    "dotenv",
    "pytest",
]


def check_dependencies():
    missing = []

    for package in REQUIRED_PACKAGES:
        try:
            importlib.import_module(package)
        except ImportError:
            missing.append(package)

    if missing:
        print("Missing dependencies:")
        for package in missing:
            print(f"- {package}")
        return False

    print("All required dependencies are installed.")
    return True


if __name__ == "__main__":
    raise SystemExit(0 if check_dependencies() else 1)