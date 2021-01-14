import os

from appdirs import AppDirs


APP_DATA_PATH = AppDirs('embargoedit', 'embargoedit').user_data_dir

RESOURCE_PATH = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)
    ),
    'resources',
)

ICON_PATH = os.path.join(
    RESOURCE_PATH,
    'icon.png',
)

ICONS_PATH = os.path.join(
    RESOURCE_PATH,
    'icons',
)
