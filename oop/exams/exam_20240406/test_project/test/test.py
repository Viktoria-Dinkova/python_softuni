from unittest import TestCase, main

from project.social_media import SocialMedia

class TestSocialMedia(TestCase):
    def setUp(self):
        self.socialmedia = SocialMedia('gosho','Instagram', followers=100, content_type='post')

    def test_correct_init(self):
        self.assertEqual('gosho', self.socialmedia._username)
        self.assertEqual('Instagram', self.socialmedia.platform)
        self.assertEqual(100, self.socialmedia.followers)
        self.assertEqual('post', self.socialmedia._content_type)
        self.assertEqual([], self.socialmedia._posts)

    def test_raise_error_whit_not_valid_platform(self):
        expected = "Platform should be one of ['Instagram', 'YouTube', 'Twitter']"

        with self.assertRaises(ValueError) as ve:
            self.socialmedia.platform = "mine"

        self.assertEqual(expected, str(ve.exception))

    def test_raise_valueerror_with_negative_followers(self):
        expected = "Followers cannot be negative."

        with self.assertRaises(ValueError) as ve:
            self.socialmedia.followers = -1

        self.assertEqual(expected, str(ve.exception))

    def test_create_post(self):
        expected = f"New {self.socialmedia._content_type} post created by {self.socialmedia._username} on {self.socialmedia._platform}."
        self.assertEqual(expected, self.socialmedia.create_post('this is my post'))
        self.assertEqual([{'content': 'this is my post', 'likes': 0, 'comments': []}], self.socialmedia._posts)

    def test_like_post_invalid_post_index(self):
        expected = "Invalid post index."

        self.assertEqual(expected, self.socialmedia.like_post(2))

    def test_like_post_with_valid_index_lower_then_possible_max_level_of_likes(self):
        self.socialmedia._posts = [{'content': 'this is my post', 'likes': 0, 'comments': []}]
        expected = f"Post liked by {self.socialmedia._username}."

        self.assertEqual(expected, self.socialmedia.like_post(0))

    def test_like_post_with_valid_index_and_max_level_of_likes(self):
        self.socialmedia._posts = [{'content': 'this is my post', 'likes': 10, 'comments': []}]
        expected = "Post has reached the maximum number of likes."

        self.assertEqual(expected, self.socialmedia.like_post(0))

    def test_comment_on_post_with_short_comment_lower_by_10_chars(self):
        self.socialmedia._posts = [{'content': 'this is my post', 'likes': 10, 'comments': []}]
        expected = "Comment should be more than 10 characters."

        self.assertEqual(expected, self.socialmedia.comment_on_post(0, 'haha'))

    def test_comment_on_post_with_proper_len_of_comment(self):
        self.socialmedia._posts = [{'content': 'this is my post', 'likes': 10, 'comments': []}]
        expected = f"Comment added by {self.socialmedia._username} on the post."

        self.assertEqual(expected, self.socialmedia.comment_on_post(0, 'this is a proper comment'))




if __name__ == '__main__':
    main()
