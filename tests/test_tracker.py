import builtins
from types import SimpleNamespace

import kpost_trace.tracker as tracker


def test_to_dataframe(tmp_path, monkeypatch):
    sample_xml = """
    <trackingInfo>
        <item>
            <eventvmd>20210601</eventvmd>
            <eventhms>1200</eventhms>
        </item>
    </trackingInfo>
    """
    def fake_parse(xml):
        return {
            "trackingInfo": {
                "item": [
                    {"eventvmd": "20210601", "eventhms": "1200"},
                ]
            }
        }

    monkeypatch.setattr(tracker.xmltodict, "parse", fake_parse)
    monkeypatch.setattr(tracker.requests, "get", lambda *a, **k: SimpleNamespace(text=sample_xml, status_code=200, raise_for_status=lambda: None))
    monkeypatch.setenv("KP_REGKEY", "dummy")

    data = tracker.track("123")
    df = tracker.to_dataframe(data)
    assert not df.empty
