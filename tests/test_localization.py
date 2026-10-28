import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STRING_CATALOG = ROOT / "DynamicIsland" / "Localizable.xcstrings"


class LocalizationTests(unittest.TestCase):
    def test_item_count_translations_keep_their_count(self):
        strings = json.loads(STRING_CATALOG.read_text())["strings"]
        mismatches = []

        for key, entry in strings.items():
            match = re.fullmatch(r"(\d+) items", key)
            if not match:
                continue
            for language, localization in entry.get("localizations", {}).items():
                value = localization.get("stringUnit", {}).get("value", "")
                if not re.search(rf"(?<!\d){match.group(1)}(?!\d)", value):
                    mismatches.append(f"{language}: {key!r} -> {value!r}")

        self.assertEqual([], mismatches)


if __name__ == "__main__":
    unittest.main()
