
# ====================
# Metadata: hint: no, time: 15m, review: no
# ====================
import base64
from typing import List
import pytest
test_cases = [
    ["Hello","World"], [""],
]

@pytest.mark.parametrize("test_input", test_cases)
def test_scenarios(test_input):
    encoded_message = Codec().encode(test_input)
    decoded_message = Codec().decode(encoded_message)
    assert encoded_message !=  decoded_message
    assert test_input == decoded_message


class Codec:

    delimiter = "&|&"

    def encode(self, strs: List[str]) -> str:
        return self.delimiter.join(strs)

    def decode(self, encoded_str: str) -> List[str]:
        return encoded_str.split(self.delimiter)

