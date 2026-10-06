import runpy
from pathlib import Path

import pytest

SCRIPT = str(Path(__file__).with_name("simple_sort.py"))
SAMPLE = ["5", "2", "1", "5", "4", "3"]


def run_script(monkeypatch, capsys, inputs):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda *a: next(it))
    namespace = runpy.run_path(SCRIPT)
    return capsys.readouterr().out.splitlines(), namespace


def test_example1_output(monkeypatch, capsys):
    lines, _ = run_script(monkeypatch, capsys, SAMPLE)
    assert lines == ["1 2 3 4 5", "1 2 3 4 5", "1 2 3 4 5"]


@pytest.mark.parametrize("name", ["insertion_sort", "selection_sort", "bubble_sort"])
def test_each_sort_does_not_mutate_input(monkeypatch, capsys, name):
    _, ns = run_script(monkeypatch, capsys, SAMPLE)
    data = [2, 1, 5, 4, 3]
    assert ns[name](data) == [1, 2, 3, 4, 5]
    assert data == [2, 1, 5, 4, 3]


@pytest.mark.parametrize("name", ["insertion_sort", "selection_sort", "bubble_sort"])
@pytest.mark.parametrize("data", [[], [1], [3, 3, 1], [5, 4, 3, 2, 1]])
def test_edge_cases(monkeypatch, capsys, name, data):
    _, ns = run_script(monkeypatch, capsys, SAMPLE)
    assert ns[name](data) == sorted(data)
