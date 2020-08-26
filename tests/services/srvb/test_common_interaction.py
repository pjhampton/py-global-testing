from services.srvb import goodbye

def test_uppercasing_a_string_from_common_lib():
    assert goodbye.common_call("sarah") == "HELLO, SARAH!"