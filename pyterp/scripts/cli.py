import click

import pyterp

extensions = {"bf": "Brainfuck"}


@click.command('pyterp')
@click.argument('filename', default="main.bf", type=str)
@click.option('--direct', default=None, type=str)
@click.option('--language', default=None, type=click.Choice(['bf']))
def cli(filename, direct, language):
    # TODO: Flesh this description out
    """
    Runs the program
    :param language:
    :param filename:
    :param direct:
    :return:
    """
    file_extension = filename.split(".")[-1]
    if file_extension not in extensions.keys():
        error = "{} is not currently supported in Pyterp.\n Pyterp currently only supports" \
                "the following types: {}".format(file_extension, extensions.items())
        raise RuntimeError(error)

    if direct is not None and language is None:
        raise click.BadOptionUsage('--language',
                                   "When running a program directly from string, you must specify the langauge "
                                   "with the --language option: Valid options include [bf]")
    """
    TODO: Figure out how to best load each interpreter based on extension. Maybe a factory?
    """
    interpreter = pyterp.Brainfuck(filename=filename, direct_input=direct)
    interpreter.run()
