from tools.tool1 import toolone

def test_tool_one_print():
    assert toolone.print_usage() == "I'm tool one!"
