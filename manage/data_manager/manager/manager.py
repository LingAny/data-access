from manager.commands import setup_reflections
from manager.conf.env_congigure_facotry import EnvConfigureFactory


def manage():
    conf = EnvConfigureFactory.create()
    setup_reflections.setup(conf)


if __name__ == '__main__':
    manage()
