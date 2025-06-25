"""Demo script for kpost_trace module."""
import os
from kpost_trace.tracker import track, to_dataframe


def main():
    os.environ.setdefault("KP_REGKEY", "your_service_key")
    tracking_no = "8671234567890"  # example tracking number
    data = track(tracking_no)
    df = to_dataframe(data)
    print(df.head())


if __name__ == "__main__":
    main()
