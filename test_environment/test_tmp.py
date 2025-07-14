def test_dodawanie():
    x = 1
    y = 10
    expected = 11
    result = x + y
    print(expected == result)
    assert expected == result #assert = oczekuj że except = result
    # if expected == result:
    #     print("PASS") #return 0
    # else:
    #     print("FAIL") #raise AssertionError - wskazuje wyjątek
