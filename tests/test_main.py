import sys
from app import main


def test_highest_count():
    assert main.highest_count('wooo hooo') == ('o', 6)

def test_several_highest_counts_tiebreaker():
    assert main.highest_count('who') == ('o', 1)

def test_edge_cases():
    assert main.highest_count('') == None
    assert main.highest_count(None) == None

def test_main(mocker):
    mocker.patch.object(sys, 'argv', [None, "woooo hoooo"])
    mock_highest_count = mocker.patch("app.main.highest_count")
    mock_print = mocker.patch("builtins.print")
    
    mock_highest_count.return_value = ('x', 17)

    main.main()

    mock_highest_count.assert_called_once_with("woooo hoooo")
    mock_print.assert_called_once_with(('x', 17))
