import os

from pipeline.report_stage import save_report, save_json_report


def test_report_creation(tmp_path):

    results = [
        {
            "port": 22,
            "state": "OPEN",
            "banner": "SSH"
        }
    ]

    txt_file = save_report(
        "127.0.0.1",
        results
    )

    json_file = save_json_report(
        "127.0.0.1",
        results
    )

    assert os.path.exists(txt_file)

    assert os.path.exists(json_file)
