#!/usr/bin/env python3
"""Wyoming API 확인"""
import wyoming.info

print("=" * 50)
print("Wyoming 라이브러리 정보")
print("=" * 50)
print(f"Wyoming 버전: {wyoming.__version__ if hasattr(wyoming, '__version__') else 'Unknown'}")
print()

print("wyoming.info 모듈에서 사용 가능한 클래스:")
print("-" * 50)
for name in dir(wyoming.info):
    if not name.startswith('_'):
        obj = getattr(wyoming.info, name)
        if isinstance(obj, type):  # 클래스만
            print(f"  - {name}")

print()
print("=" * 50)