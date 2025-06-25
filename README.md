# Track-a-waybill

Python utilities for tracking Korean postal shipments using the Korea Post open API.

## Features
- Unified `track()` function for domestic and international shipments.
- Simple conversion to `pandas.DataFrame` for analysis.
- Example script and basic tests provided.

## Usage
```
pip install requests xmltodict pandas

export KP_REGKEY="your_service_key"
python examples/demo.py  # 저장소 루트에서 실행

# 테스트 실행
python -m pytest -q
```
