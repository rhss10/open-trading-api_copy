# NOTE: 보안성을 위해서는 DB조회 및 메모리로 인증정보를 관리하는것을 추천드립니다
# kis_domstk module 을 찾을 수 없다는 에러가 나는 경우 sys.path에 kis_domstk.py 가 있는 폴더를 추가해준다.
import sys

import yaml

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

sys.path.append(config["CONFIG_ROOT"])
import kis_auth as ka
import kis_ovrseastk as ko
import pandas as pd

ITEM_NO = "00700"
# 토큰 발급
ka.auth(svr="vps")

# [국내주식] 주문/계좌 > 주식현금주문 (매수매도구분 buy,sell + 종목번호 6자리 + 주문수량 + 주문단가)
# 지정가 기준이며 시장가 옵션(주문구분코드)을 사용하는 경우 kis_domstk.py get_order_cash 수정요망!
# NOTE: 예시는 홍콩
# rt_data = ko.get_overseas_order(
#     ord_dv="buy", excg_cd="SHEK", itm_no=ITEM_NO, qty=100, unpr=389.200
# )
# print(
#     rt_data.KRX_FWDG_ORD_ORGNO + "+" + rt_data.ODNO + "+" + rt_data.ORD_TMD
# )  # 주문접수조직번호+주문접수번호+주문시각

# [국내주식] 주문/계좌 > 주식일별주문체결(현황)조회
# dv="01"   01:3개월 이내 국내주식체결내역 (월단위 ex: 2024.04.25 이면 2024.01월~04월조회)
# dv="02"   02:3개월 이전 국내주식체결내역 (월단위 ex: 2024.04.25 이면 2024.01월이전)
rt_data = ko.get_overseas_inquire_ccnl()
print(rt_data)
