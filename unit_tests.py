import unittest
from unittest.mock import patch, Mock
from posts_proj import *

class TestJSONPosts(unittest.TestCase):
    @patch('requests.get')
    def test_get_random_posts(self, mock_get):
        mock_get.return_value.json.return_value = [{'id': i, 'title': f'title{i}'} for i in range(100)] # Mock the response from requests.get
        posts = get_random_posts()
        self.assertEqual(len(posts), 10) # Assert that the function returns 10 posts

    @patch('requests.get')
    def test_print_specific_post(self, mock_get):
        mock_get.return_value.json.return_value = {'title': 'test_title', 'body': 'test_body'}
        with patch('builtins.print') as mock_print:
            print_specific_post(1)
        # Assert that the print function was called with the correct arguments
        # the \033 is due to BOLD text being printed
        mock_print.assert_any_call('\033[1m\nPost:\033[0m')
        mock_print.assert_any_call('test_title\n')
        mock_print.assert_any_call('\033[1mBody:\033[0m')
        mock_print.assert_any_call('test_body\n')

    @patch('requests.get')
    def test_print_post_comments(self, mock_get):
        mock_get.return_value.json.return_value = [{'name': 'test_name', 'body': 'test_body'}]
        with patch('builtins.print') as mock_print:
            print_post_comments(1)
        mock_print.assert_any_call('\ntest_name:test_body')

    @patch('requests.post')
    def test_publish_comment(self, mock_post):
        mock_post.return_value.status_code = 201
        with patch('builtins.print') as mock_print:
            publish_comment(1, 'test_comment', 'test_name', 'test_email')
        mock_print.assert_any_call('\nComment published successfully!')

if __name__ == '__main__':
    unittest.main(verbosity=2) # Verbosity prints extra info