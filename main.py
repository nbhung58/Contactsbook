# _*_ coding: utf-8 _*_
# rpcontacts/main.py

"""This module provides RP Contact Application."""

import sys
from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .Views import Window


def main():
    """Rp contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create the main window if the connection succeeded
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())
