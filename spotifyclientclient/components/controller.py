from __future__ import annotations

import subprocess
import typing

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget

from spotifyclientclient.utils.actions import WithActions


class SpotifyController(QWidget, WithActions):

    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self._next_action = self._create_action(
            'next',
            lambda: self.dbus_send(
                'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next',
            ),
            'Right',
        )
        self._previous_action = self._create_action(
            'next',
            lambda: self.dbus_send(
                'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous',
            ),
            'Left',
        )
        self._toggle_pause_action = self._create_action(
            'next',
            lambda: self.dbus_send(
                'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause',
            ),
            'Space',
        )

        self._next_button = QtWidgets.QPushButton('Next')
        self._previous_button = QtWidgets.QPushButton('Previous')
        self._toggle_pause_button = QtWidgets.QPushButton('Pause / Play')

        for button, action in (
            (self._next_button, self._next_action),
            (self._previous_button, self._previous_action),
            (self._toggle_pause_button, self._toggle_pause_action),
        ):
            button.clicked.connect(action.trigger)
            # button.setFocusPolicy(QtCore.Qt.NoFocus)

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self._next_button)
        layout.addWidget(self._previous_button)
        layout.addWidget(self._toggle_pause_button)

    @classmethod
    def dbus_send(cls, s: str) -> None:
        subprocess.run(
            s,
            shell = True,
        )
