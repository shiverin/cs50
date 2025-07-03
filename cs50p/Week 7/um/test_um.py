from um import count

def test_1():
    assert count("umum")==0

def test_2():
    assert count(" um ")==1
def test_3():
    assert count(" Um")==1
