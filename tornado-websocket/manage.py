import click
from main import main

@click.group()
def manage():
    pass

@click.command()
@click.option('-p', '--port', default=8000,
              help=('run server on port default 8000'))
@click.option('-w', '--worker', default=1,
              help=('run server as multi prosess default 1'))
@click.option('--debug', default=False, is_flag=True,
              help=('debug mode default Fals'))
@click.option('--doc', default=False, is_flag=True,
              help=('debug mode default Fals'))
@click.option('--timeout', default=2,
              help=('server timeout default 2'))
def run(**kwargs):
    main(**kwargs)

manage.add_command(run, 'run')

if __name__ == '__main__':
    manage()