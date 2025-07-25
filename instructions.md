# gdi_template_app

## How to use?
1. If you want to use the pytoolkit package, you need to execute the following command first:
    python -m pip install pytoolkit

## Folder Structure

```
__init__.py               # Package initialization file
const.py                  # Global constants
IFU.md                    # Instruction file for the project
logger.py                 # Logging configuration and utilities
main.py                   # Main entry point of the application
README.md                 # Project documentation
requirements.txt          # Python dependencies
tools.py                  # Utility tools for the project

app/                      # Application-specific modules
    __init__.py           # Package initialization file
    config/               # Configuration files and utilities
        __init__.py       # Package initialization file
        config.yaml       # YAML configuration file
        read_config.py    # Script to read configuration
    controllers/          # Controllers for handling business logic
        __init__.py       # Package initialization file
        main_controller.py    # Main application controller
    entity/               # Data models and entities
        __init__.py       # Package initialization file
    services/             # Core services and business logic
        __init__.py       # Package initialization file
ui/                       # User interface components
    __init__.py           # Package initialization file
utils/                    # Utility functions and helpers
    __init__.py           # Package initialization file

components/               # Reusable components

core/                     # Core framework and base classes
    __init__.py           # Package initialization file

logs/                     # Log files

resources/                # Static resources
    __init__.py           # Package initialization file

test/                     # Test cases
    __init__.py           # Package initialization file
```

## Libraries and Frameworks

- Pyside2 and QSS for the frontend.
- Python for the backend.