from pathlib import Path


def test_sigma_pipeline_files_exist():
    assert Path("pipelines/opensearch_windows.yml").exists()
    assert Path("pipelines/opensearch_linux.yml").exists()
