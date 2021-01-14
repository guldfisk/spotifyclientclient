from __future__ import annotations

import sys

from PyQt5.QtWidgets import QMainWindow

from spotifyclientclient.application.scc import SCCApp
from spotifyclientclient.components.controller import SpotifyController


class MainWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        # self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)

        self._main_view = SpotifyController()

        self.setCentralWidget(self._main_view)


def run():
    app = SCCApp.init(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    main_window = MainWindow()

    main_window.showMaximized()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
