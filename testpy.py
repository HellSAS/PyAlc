import click

@click.command()
@click.confirmation_option(prompt='Are you sure you want to drop the db?')
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
