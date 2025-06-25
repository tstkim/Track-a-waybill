"""kpost_trace 모듈 사용 예시 스크립트."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from kpost_trace.tracker import track, to_dataframe


def main():
    regkey = os.environ.get("KP_REGKEY")
    if not regkey or regkey == "your_service_key":
        print("KP_REGKEY 환경변수가 설정되지 않았습니다.")
        return

    tracking_no = "8671234567890"  # 예시 운송장 번호

    try:
        data = track(tracking_no)
        df = to_dataframe(data)
        print(df.head())
    except Exception as e:
        print("조회 중 오류 발생:", e)


if __name__ == "__main__":
    main()
