import os
import pathlib
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class VolumeHUDIconTests(unittest.TestCase):
    def test_connected_headset_icon_only_when_it_is_the_output(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = pathlib.Path(temporary_directory)
            executable = temporary_path / "volume-hud-icon-regression"
            environment = os.environ.copy()
            environment["CLANG_MODULE_CACHE_PATH"] = str(temporary_path / "module-cache")
            environment["SWIFT_MODULECACHE_PATH"] = str(temporary_path / "module-cache")
            subprocess.run(
                [
                    "swiftc",
                    str(ROOT / "DynamicIsland/components/OSD/VolumeHUDIcon.swift"),
                    str(ROOT / "tests/VolumeHUDIconRegression.swift"),
                    "-o",
                    str(executable),
                ],
                check=True,
                cwd=ROOT,
                env=environment,
            )
            subprocess.run([str(executable)], check=True, cwd=ROOT)


if __name__ == "__main__":
    unittest.main()
