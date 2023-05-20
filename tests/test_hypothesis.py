import unittest
import os
import json

from hypothesis import given, settings
import hypothesis.strategies as st

from main import file_path
from elias_decoding import elias_decoding
from elias_encoding import elias_encoding
from test_memory import total_size


class BasicTestCase(unittest.TestCase):
    @given(st.just(file_path))
    @settings(deadline=None)
    def test_file_existance(self, file_path_):
        self.assertEqual(os.path.exists(file_path_), False)

    @given(st.just(file_path), st.just('utf-8'))
    @settings(deadline=6000)
    def test_file_encoding(self, file_path_, encoding_):
        with open("../" + file_path_, 'r', encoding=encoding_) as f:
            data = f.readline(1024)
        self.assertIsNotNone(data)

    @given(st.just(file_path), st.just('utf-8'))
    @settings(deadline=6000)
    def test_file_json_parsing(self, file_path_, encoding_):
        with open("../" + file_path_, 'r', encoding=encoding_) as f:
            data = f.readline()
        json_data = json.loads(data)
        self.assertIsNotNone(json_data)


class DataContentTest(unittest.TestCase):
    @given(st.just(file_path), st.just('utf-8'))
    @settings(deadline=6000)
    def test_file_has_post(self, file_path_, encoding_):
        is_text_found = False
        with open("../" + file_path_, 'r', encoding=encoding_) as f:
            for line in f:
                is_text_found = ('"text":' in line) or is_text_found
                if is_text_found:
                    break

        self.assertEqual(is_text_found, True)

    @given(st.just(file_path), st.just('utf-8'), st.just(40000))
    @settings(deadline=6000)
    def test_file_posts_count(self, file_path_, encoding_, req_elem_count):
        el_found = 0
        with open("../" + file_path_, 'r', encoding=encoding_) as f:
            for line in f:
                el_found += line.count('"text":')
                if el_found >= req_elem_count:
                    break

        self.assertGreaterEqual(el_found, req_elem_count)

    @given(st.just(file_path), st.just('utf-8'), st.sampled_from(['text', '_id', 'post_author_id', 'likes_count']))
    @settings(deadline=6000)
    def test_file_has_attribute(self, file_path_, encoding_, attribute_):
        is_text_found = False
        with open("../" + file_path_, 'r', encoding=encoding_) as f:
            for line in f:
                is_text_found = (('"' + attribute_ + '"') in line)
                if is_text_found:
                    break

        self.assertEqual(is_text_found, True)

    @given(st.just(file_path), st.just('utf-8'), st.sampled_from(['СПбГУ', 'Ректор', 'Университет']))
    @settings(deadline=6000)
    def test_file_has_mentions(self, file_path_, encoding_, phrase_):
        is_text_found = False
        with open("../" + file_path_, 'r', encoding=encoding_) as f:
            for line in f:
                is_text_found = (phrase_ in line) or is_text_found

        self.assertEqual(is_text_found, True)


class MethodsTestCases(unittest.TestCase):
    @given(st.integers(min_value=1, max_value=10000), st.integers(min_value=1, max_value=2))
    @settings(deadline=6000)
    def test_encode_return_type(self, value_sample, encoding_type):
        encoded = elias_encoding(value_sample, encoding_type)
        self.assertIsInstance(encoded, str)

    @given(st.binary(min_size=1, max_size=20), st.integers(min_value=1, max_value=2))
    @settings(deadline=6000)
    def test_decode_return_type(self, value_sample, encoding_type):
        decoded = elias_decoding(str(value_sample), encoding_type)
        self.assertIsInstance(decoded, int)

    @given(st.text())
    @settings(deadline=6000)
    def test_memory_return_type(self, value_sample):
        size = total_size(value_sample)
        self.assertIsInstance(size, int)


class DataProcessingTestCases(unittest.TestCase):
    @given(st.integers(min_value=1, max_value=10000), st.integers(min_value=1, max_value=2))
    @settings(deadline=6000)
    def test_encode_decode_pair(self, value_sample, encoding_type):
        encoded = elias_encoding(value_sample, encoding_type)
        decoded = elias_decoding(encoded, encoding_type)
        self.assertEqual(value_sample, decoded)


if __name__ == '__main__':
    unittest.main()
