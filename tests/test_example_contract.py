import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
EXAMPLE = ROOT / "examples" / "01-cmd-basics"


class SagaExampleContractTests(unittest.TestCase):

    def _run_with_fake_saga(self, payload, exit_code=0, executable=True):
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            bin_dir = temp_path / "bin"
            bin_dir.mkdir()
            fake = bin_dir / "saga_cmd"
            if executable:
                fake.write_text(
                    "#!/usr/bin/env bash\n"
                    + "printf '%s' " + repr(payload) + "\n"
                    + "exit " + str(exit_code) + "\n",
                    encoding="utf-8",
                )
                fake.chmod(0o755)
            env = os.environ.copy()
            env["PATH"] = str(bin_dir) + os.pathsep + os.defpath
            output = temp_path / "cli-help.txt"
            result = subprocess.run(
                ["bash", str(EXAMPLE / "inspect-cli.sh"), str(output)],
                env=env, capture_output=True, text=True, check=False, timeout=10,
            )
            content = output.read_text(encoding="utf-8") if output.exists() else ""
            return result, content

    def test_cli_accepts_identifying_help_even_if_saga_returns_nonzero(self):
        result, content = self._run_with_fake_saga("SAGA Command Line Usage", exit_code=1)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SAGA Command Line Usage", content)

    def test_cli_rejects_empty_or_unrelated_output(self):
        empty_result, _ = self._run_with_fake_saga("")
        self.assertNotEqual(empty_result.returncode, 0)
        unrelated_result, _ = self._run_with_fake_saga("unrelated tool output")
        self.assertNotEqual(unrelated_result.returncode, 0)

    def test_cli_fails_clearly_when_binary_is_missing(self):
        result, _ = self._run_with_fake_saga("", executable=False)
        self.assertEqual(result.returncode, 127)
        self.assertIn("saga_cmd was not found", result.stderr)

    def test_cli_example_has_usage_and_validation_boundary(self):
        readme = (EXAMPLE / "README.md").read_text(encoding="utf-8")
        script = (EXAMPLE / "inspect-cli.sh").read_text(encoding="utf-8")
        self.assertIn("bash examples/01-cmd-basics/inspect-cli.sh", readme)
        self.assertIn("command -v saga_cmd", script)
        self.assertIn("-s \"$output_path\"", script)
        self.assertIn("grep -qi 'saga'", script)


if __name__ == "__main__":
    unittest.main()
