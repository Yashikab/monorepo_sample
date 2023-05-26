import logic1.hello as hello


def test_say_hello():
    target_msg = "hi"
    expected = "hello, hi"
    actual = hello.say_hello(target_msg)
    assert expected == actual
