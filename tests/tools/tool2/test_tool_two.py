from tools.tool2 import tooltwo

def test_tool_one_print():
    assert tooltwo.print_usage() == "Howdy! I'm tool 2"
