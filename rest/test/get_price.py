# kis_domstk module 을 찾을 수 없다는 에러가 나는 경우 sys.path에 kis_domstk.py 가 있는 폴더를 추가해준다.
import sys

sys.path.append(CONFIG_ROOT)
import pandas as pd

import rest.kis_auth as ka
import Sample01.kis_domstk as kb

# 토큰 발급
ka.auth(svr="vps")

# [국내주식] 기본시세 > 주식현재가 시세 (종목번호 6자리)
rt_data = kb.get_inquire_price(itm_no="071050")
print(rt_data.stck_prpr + " " + rt_data.prdy_vrss)  # 현재가, 전일대비
