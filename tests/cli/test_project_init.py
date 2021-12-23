from click.testing import CliRunner
from art_engine.commands.cmd_init import cli
import shutil
import os


def test_it_creates_a_simple_project():
    runner = CliRunner()
    result = runner.invoke(cli, ["simple-test-dir", "--project-type", "simple"])
    assert result.exit_code == 0
    assert "Done ..." in result.output
    assert os.path.isdir("simple-test-dir")
    assert os.path.isdir("simple-test-dir/layers/simple")
    assert not os.path.isdir("simple-test-dir/layers/complex")


def test_it_creates_a_complex_project():
    runner = CliRunner()
    result = runner.invoke(cli, ["complex-test-dir", "--project-type", "complex"])
    assert result.exit_code == 0
    assert "Done ..." in result.output
    assert os.path.isdir("complex-test-dir")
    assert os.path.isdir("complex-test-dir/layers/simple")
    assert os.path.isdir("complex-test-dir/layers/complex")


def teardown_module(module):
    shutil.rmtree("simple-test-dir")
    shutil.rmtree("complex-test-dir")
