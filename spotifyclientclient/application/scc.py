from __future__ import annotations

import os
import typing
import re
import typing as t

from PyQt5.QtWidgets import QApplication

from spotifyclientclient import paths


class SCCApp(QApplication):
    current: t.Optional[SCCApp]

    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)
        with open(os.path.join(paths.RESOURCE_PATH, 'style.qss'), 'r') as f:
            icon_path = os.path.join(
                paths.RESOURCE_PATH,
                'qss_icons',
                'rc',
                '',
            ).replace('\\', '/')

            pattern = re.compile('url\((.*)\)')

            r = pattern.sub(f'url("{icon_path}\\1")', f.read())

            self.setStyleSheet(r)

        self.setOrganizationDomain('prohunterdogkeeper.dk')
        self.setApplicationName('SCC')

    @classmethod
    def init(cls, argv: typing.List[str]) -> SCCApp:
        cls.current = cls(argv)
        return cls.current
