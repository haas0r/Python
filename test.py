def test_substring(full_string, substring):
    assert substring in full_string, f'expected {substring} to be substring of {full_string}'


x = 'some_text'
y = 'some'

test_substring(x,y)