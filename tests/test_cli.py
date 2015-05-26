from click.testing import CliRunner

from pyfck.scripts.cli import cli


def test_bare_command():
    """
    This test checks that if you just run pyfck by itself, it should pick up a main.bf file and run it
    :return:
    """
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    # Test for a hello world in brainfuck
    assert result.output == "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.\n"


def test_direct_input():
    """
    This test checks that the direct input option for pyfck is working
    :return:
    """
    hello_world = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>" \
                   ">+.>++.\n"
    runner = CliRunner()
    result = runner.invoke(cli, ['--direct', hello_world])
    assert result.exit_code == 0
    assert result.output == hello_world


def test_file_input():
    """
    This will test the file input portion of pyfck
    :return:
    """
    right_filename = "main.bf"
    wrong_filename = "wrong.bf"
    runner = CliRunner()
    result = runner.invoke(cli, [right_filename])
    assert result.exit_code == 0
    assert result.output == "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------." \
                            "--------.>>+.>++.\n"
    result = runner.invoke(cli, [wrong_filename])
    assert result.exit_code == 1
    assert result.output == "Cannot open file {}\n".format(wrong_filename)