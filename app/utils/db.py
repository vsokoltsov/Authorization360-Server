import os
from pathlib import Path

from alembic import script
from alembic.config import Config
from alembic import command
from alembic.runtime import migration
import sqlalchemy

from app.config import get_database_path
from app.logger import logger


def get_alembic_config():
    """ Get alembic config. """

    alembic_conf_path = os.path.join(
        Path(__file__).parent.parent.parent, 'alembic', 'alembic.ini'
    )
    return Config(alembic_conf_path)

def run_migrations():
    """ Run migrations programatically. Check whethere they were runned before """

    database_path = get_database_path()
    alembic_cfg = get_alembic_config()
    alembic_cfg.set_main_option('sqlalchemy.url', database_path)
    engine = sqlalchemy.create_engine(database_path)
    script_ = script.ScriptDirectory.from_config(alembic_cfg)
    with engine.begin() as conn:
        context = migration.MigrationContext.configure(conn)
        if context.get_current_revision() != script_.get_current_head():
            command.upgrade(alembic_cfg, "head")
