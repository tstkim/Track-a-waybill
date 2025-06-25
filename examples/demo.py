"""kpost_trace 모듈 사용 예시 스크립트."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from kpost_trace.tracker import track, to_dataframe


def main():
    os.environ.setdefault("KP_REGKEY", "your_service_key")
    tracking_no = "8671234567890"  # example tracking number
    data = track(tracking_no)
    df = to_dataframe(data)
    print(df.head())


if __name__ == "__main__":
    main()
