import pyfck


def test_open_file():
    """
    Test that pyfck is properly opening and parsing the given source file in the tests folder
    :return:
    """
    the_file = "main.bf"
    interpreter = pyfck.Interpreter(filename=the_file)
    assert interpreter.source_file == the_file
    assert interpreter.program == "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."


def test_direct_input():
    """
    Test that pyfck is properly parsing a direct input string
    :return:
    """
    hello_brainfuck = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    interpreter = pyfck.Interpreter(direct_input=hello_brainfuck)
    assert interpreter.program == hello_brainfuck

def test_rot_13():
    filename = "rot13.bf"
    interpreter = pyfck.Interpreter(filename=filename)
    print interpreter.program

if __name__ == "__main__":
    test_rot_13()