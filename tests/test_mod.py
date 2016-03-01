import pyterp


def test_open_file():
    """
    Test that pyterp is properly opening and parsing the given source file in the tests folder
    :return:
    """
    the_file = "main.bf"
    interpreter = pyterp.Brainfuck(filename=the_file)
    assert interpreter.source_file == the_file
    assert interpreter.program == "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>--" \
                                  "-.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."


def test_direct_input():
    """
    Test that pyterp is properly parsing a direct input brainfuck string
    :return:
    """
    hello_brainfuck = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---." \
                      "+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    interpreter = pyterp.Brainfuck(direct_input=hello_brainfuck)
    assert interpreter.program == hello_brainfuck


def test_rot_13():
    filename = "rot13.bf"
    interpreter = pyterp.Brainfuck(filename=filename)
    print interpreter.program

if __name__ == "__main__":
    test_rot_13()