# 금융 데이터
import sys
import time

import yaml

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

sys.path.append(config["CONFIG_ROOT"])
import kis_auth as ka
import kis_domstk as kb
import pandas as pd

ITEM_NO = "360750"
CURR_DATE = "20240919"

# 토큰 발급
ka.auth(svr="vps")

# 주식 종목 및 시장 데이터
# 시가, 고가, 저가, 종가, 거래량
daily_price = kb.get_inquire_daily_price(itm_no=ITEM_NO)
print(
    "시가:",
    daily_price[daily_price["stck_bsop_date"] == CURR_DATE]["stck_oprc"].values[0],
)
print(
    "고가:",
    daily_price[daily_price["stck_bsop_date"] == CURR_DATE]["stck_hgpr"].values[0],
)
print(
    "저가:",
    daily_price[daily_price["stck_bsop_date"] == CURR_DATE]["stck_lwpr"].values[0],
)
print(
    "종가:",
    daily_price[daily_price["stck_bsop_date"] == CURR_DATE]["stck_clpr"].values[0],
)
print(
    "거래량:",
    daily_price[daily_price["stck_bsop_date"] == CURR_DATE]["acml_vol"].values[0],
)

# 외국인, 기관, 개인, 프로그램 순매수/순매도 거래량
# 기본 정보와 다르게 장이 끝나야 데이터가 나오는 듯
time.sleep(2)

# daily_program_investor = kb.get_inquire_price(itm_no=ITEM_NO)
daily_investor = kb.get_inquire_investor(itm_no=ITEM_NO)
daily_investor.to_csv("daily_investor.csv", index=False)
print(
    "개인 순매수 수량:",
    daily_investor[daily_investor["stck_bsop_date"] == CURR_DATE][
        "prsn_ntby_qty"
    ].values[0],
)
print(
    "개인 매도 거래량:",
    daily_investor[daily_investor["stck_bsop_date"] == CURR_DATE][
        "prsn_seln_vol"
    ].values[0],
)
print(
    "외인 순매수 수량:",
    daily_investor[daily_investor["stck_bsop_date"] == CURR_DATE][
        "frgn_ntby_qty"
    ].values[0],
)
print(
    "외인 매도 거래량:",
    daily_investor[daily_investor["stck_bsop_date"] == CURR_DATE][
        "frgn_seln_vol"
    ].values[0],
)
print(
    "기관 순매수 수량:",
    daily_investor[daily_investor["stck_bsop_date"] == CURR_DATE][
        "orgn_ntby_qty"
    ].values[0],
)
print(
    "기관 매도 거래량:",
    daily_investor[daily_investor["stck_bsop_date"] == CURR_DATE][
        "orgn_seln_vol"
    ].values[0],
)

# 공매도 비율

# 보조지표, 차트 패턴
