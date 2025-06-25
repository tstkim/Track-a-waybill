from __future__ import annotations
import os
from typing import Literal, Dict

import requests
import xmltodict
import pandas as pd

BASE_URL = "https://biz.epost.go.kr/KpostPortal/openapi"


def track(
    tracking_no: str,
    *,
    target: Literal["trace", "emsTrace", "emsEngTrace", "traceOrdNo"] = "trace",
    service_key: str | None = None,
    show_rec: str | None = None,
) -> Dict:
    """우체국 종추적(Open API) 조회 함수."""
    service_key = service_key or os.getenv("KP_REGKEY")
    if not service_key:
        raise RuntimeError("KP_REGKEY 환경변수 또는 service_key 인자를 지정해 주세요.")

    params = {
        "regkey": service_key,
        "target": target,
        "query": tracking_no,
    }
    if show_rec is not None:
        params["showRec"] = show_rec

    res = requests.get(BASE_URL, params=params, timeout=10)
    res.raise_for_status()
    data = xmltodict.parse(res.text)

    if "error" in data:
        code = data["error"].get("error_code")
        msg = data["error"].get("message")
        raise RuntimeError(f"[{code}] {msg}")

    return data


def to_dataframe(resp: Dict) -> pd.DataFrame:
    """종추적 XML을 DataFrame으로 변환"""
    items = resp["trackingInfo"]["item"]
    return pd.DataFrame(items)


if __name__ == "__main__":
    # Example usage for manual testing. Ensure KP_REGKEY is set.
    df = to_dataframe(track("8671234567890"))
    print(df.head())
