import click


@click.group()
def db():
    """Perform database migrations."""
    pass


@click.command()
@click.option('-d', '--directory', default=None,
              help=('migration script directory (default is "migrations")'))
@click.option('--multidb', is_flag=True,
              help=('Support multiple databases'))
def init(directory, multidb):
    """Creates a new migration repository."""
    print 'init'


db.add_command(init)