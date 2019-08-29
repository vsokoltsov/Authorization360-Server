import os
from pathlib import Path
from alembic.config import Config
from app.config import get_database_path
from alembic import command

def run_migrations():
    """ Run migrations programatically. """

    alembic_conf_path = os.path.join(
        Path(__file__).parent.parent.parent, 'alembic', 'alembic.ini'
    )
    alembic_cfg = Config(alembic_conf_path)
    alembic_cfg.set_main_option('sqlalchemy.url', get_database_path())
    command.upgrade(alembic_cfg, "head")
