# API call wrapping
# API응답처리 공통
class APIResp:
    # 응답코드, 응답헤더, Output, 오류코드, 오류메시지
    def __init__(self, resp):
        self._rescode = resp.status_code
        self._resp = resp
        self._header = self._setHeader()
        self._body = self._setBody()
        self._err_code = self._body.rt_cd
        self._err_message = self._body.msg1

    #
    def getResCode(self):
        return self._rescode

    def _setHeader(self):
        fld = dict()
        for x in self._resp.headers.keys():
            if x.islower():
                fld[x] = self._resp.headers.get(x)
        _th_ = namedtuple("header", fld.keys())

        return _th_(**fld)

    def _setBody(self):
        _tb_ = namedtuple("body", self._resp.json().keys())

        return _tb_(**self._resp.json())

    def getHeader(self):
        return self._header

    def getBody(self):
        return self._body

    def getResponse(self):
        return self._resp

    def isOK(self):
        try:
            if self.getBody().rt_cd == "0":
                return True
            else:
                return False
        except:
            return False

    def getErrorCode(self):
        return self._err_code

    def getErrorMessage(self):
        return self._err_message

    def printAll(self):
        # print(self._resp.headers)
        print("<Header>")
        for x in self.getHeader()._fields:
            print(f"\t-{x}: {getattr(self.getHeader(), x)}")
        print("<Body>")
        for x in self.getBody()._fields:
            print(f"\t-{x}: {getattr(self.getBody(), x)}")

    def printError(self):
        print("-------------------------------\nError in response: ", self.getResCode())
        print(self.getBody().rt_cd, self.getErrorCode(), self.getErrorMessage())
        print("-------------------------------")

    # end of class APIResp


def _url_fetch(
    api_url, ptr_id, params, appendHeaders=None, postFlag=False, hashFlag=False
):
    url = f"{getTREnv().my_url}{api_url}"

    headers = _getBaseHeader()

    # 추가 Header 설정
    tr_id = ptr_id
    if ptr_id[0] in ("T", "J", "C"):
        if isPaperTrading():
            tr_id = "V" + ptr_id[1:]

    # API별 tr_id 입니다. API문서 header부분 tr_id를 참조하세요
    headers["tr_id"] = tr_id
    # 개인고객은 무조건 'P'입니다.
    headers["custtype"] = "P"

    if appendHeaders is not None:
        if len(appendHeaders) > 0:
            for x in appendHeaders.keys():
                headers[x] = appendHeaders.get(x)

    # if(_DEBUG):
    #     print(headers)
    #     print(params)

    if _DEBUG:
        print("< Sending Info >")
        print(f"URL: {url}, TR: {tr_id}")
        print(f"<header>\n{headers}")
        print(f"<body>\n{params}")

    if postFlag:
        if hashFlag:
            set_order_hash_key(headers, params)
        res = requests.post(url, headers=headers, data=json.dumps(params))
    else:
        res = requests.get(url, headers=headers, params=params)

    if res.status_code == 200:
        ar = APIResp(res)
        if _DEBUG:
            ar.printAll()
        return ar
    else:
        print("Error Code : " + str(res.status_code) + " | " + res.text)
        return None
