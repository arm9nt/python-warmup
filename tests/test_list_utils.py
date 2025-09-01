from app.list_utils import unique

def test_unique():
    assert unique([]) == []
    assert unique([1,1,2,2,2,5]) == [1,2,5]
    assert unique([3,3,3]) == [3]
