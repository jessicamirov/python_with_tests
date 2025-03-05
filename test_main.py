# test_main.py
from main import get_website_content

def test_get_website_content():
    result = get_website_content('https://www.example.com')
    assert "Example Domain" in result
