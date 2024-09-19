# kis_domstk module 을 찾을 수 없다는 에러가 나는 경우 sys.path에 kis_domstk.py 가 있는 폴더를 추가해준다.
import sys

import yaml

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

sys.path.append(config["CONFIG_ROOT"])
import kis_auth as ka
import kis_domstk as kb
import pandas as pd

ITEM_NO = "071050"
# 토큰 발급
ka.auth(svr="vps")

# [국내주식] 기본시세 > 주식현재가 시세 (종목번호 6자리)
rt_data = kb.get_inquire_price(itm_no=ITEM_NO)
print(rt_data.stck_prpr + " " + rt_data.prdy_vrss)  # 현재가, 전일대비


# [국내주식] 기본시세 > 주식현재가 체결 (종목번호 6자리)
# rt_data = kb.get_inquire_ccnl(itm_no=ITEM_NO)
# print(rt_data)

# [국내주식] 기본시세 > 주식현재가 일자별 (종목번호 6자리 + 기간분류코드)
# 기간분류코드    D : (일)최근 30거래일  W : (주)최근 30주   M : (월)최근 30개월
# 수정주가기준이며 수정주가미반영 기준을 원하시면 인자값 adj_prc_code="2" 추가
# rt_data = kb.get_inquire_daily_price(itm_no=ITEM_NO, period_code="M")
# print(rt_data)


# # [국내주식] 기본시세 > 주식현재가 호가 (종목번호 6자리)
# rt_data = kb.get_inquire_asking_price_exp_ccn(itm_no=ITEM_NO)
# print(rt_data)

# [국내주식] 기본시세 > 주식현재가 예상체결 (출력구분="2" + 종목번호 6자리)
# rt_data = kb.get_inquire_asking_price_exp_ccn(output_dv="2", itm_no=ITEM_NO)
# print(rt_data)

# [국내주식] 기본시세 > 주식현재가 투자자 (종목번호 6자리)
# rt_data = kb.get_inquire_investor(itm_no=ITEM_NO)
# print(rt_data)

# [국내주식] 기본시세 > 주식현재가 회원사 (종목번호 6자리)
# rt_data = kb.get_inquire_member(itm_no=ITEM_NO)
# print(rt_data)

# [국내주식] 기본시세 > 국내주식기간별시세(일/주/월/년) (종목번호 6자리)
# rt_data = kb.get_inquire_asking_price_exp_ccn(itm_no=ITEM_NO)
# print(rt_data)

# [국내주식] 기본시세 > 국내주식기간별시세(일/주/월/년) (기간별 데이터 Default는 일별이며 조회기간은 100일전(영업일수 아님)부터 금일까지)
# TODO: rt_data_obj = kb.get_inquire_daily_itemchartprice(output_dv="2", itm_no=ITEM_NO)
# print(rt_data)


# [국내주식] 기본시세 > 주식현재가 당일시간대별체결 (현재가 : 주식현재가, 전일대비, 전일대비율, 누적거래량,전일거래량, 대표시장한글명))
# rt_data = kb.get_inquire_time_itemconclusion(itm_no="071050")
# print(rt_data)

# [국내주식] 기본시세 > 주식현재가 당일시간대별체결 (시간대별체결내역)
rt_data = kb.get_inquire_time_itemconclusion(
    output_dv="2", itm_no="071050"
)  # 기준시각 미지정시 현재시각 이전 체결 내역이 30건 조회됨
# rt_data = kb.get_inquire_time_itemconclusion(output_dv='2', itm_no="071050", inqr_hour='100000') # 지정 기준시각 이전 체결 내역이 30건 조회됨
print(rt_data)
