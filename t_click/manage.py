import click
import re
from cli import db

@click.group()
def manage():
    pass

@click.command()
def main():
    print '__main__'


manage.add_command(main, 'run')
manage.add_command(db, 'db')

if __name__ == '__main__':
    manage()