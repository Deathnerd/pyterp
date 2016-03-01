from click.testing import CliRunner

from pyterp.scripts.cli import cli


def test_bare_command():
    """
    This test checks that if you just run pyfck by itself, it should pick up a main.bf file and run it
    :return:
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    # Test for a hello world in brainfuck
    assert result.output == "H e l l o  W o r l d!\n"


def test_direct_input():
    """
    This test checks that the direct input option for pyfck is working
    :return:
    """
    hello_world = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>." \
                  ">---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    runner = CliRunner()
    result = runner.invoke(cli, ['--direct', hello_world])
    assert result.output == "H e l l o  W o r l d!\n"