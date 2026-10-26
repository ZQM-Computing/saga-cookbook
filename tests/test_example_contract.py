import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
EXAMPLE = ROOT / "examples" / "01-cmd-basics"


class SagaExampleContractTests(unittest.TestCase):
    def test_cli_example_has_usage_and_validation_boundary(self):
        readme = (EXAMPLE / "README.md").read_text(encoding="utf-8")
        script = (EXAMPLE / "inspect-cli.sh").read_text(encoding="utf-8")
        self.assertIn("bash examples/01-cmd-basics/inspect-cli.sh", readme)
        self.assertIn("command -v saga_cmd", script)
        self.assertIn("-s \"$output_path\"", script)
        self.assertIn("grep -qi 'saga'", script)


if __name__ == "__main__":
    unittest.main()
