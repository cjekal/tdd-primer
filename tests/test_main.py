from app.main import highest_count


def test_highest_count():
    assert highest_count('wooo hooo') == ('o', 6)

def test_several_highest_counts_tiebreaker():
    assert highest_count('who') == ('o', 1)

def test_edge_cases():
    assert highest_count('') == None
    assert highest_count(None) == None
