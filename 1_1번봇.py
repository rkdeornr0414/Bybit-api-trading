from pybit.unified_trading import HTTP
import logging
from pybit.exceptions import InvalidRequestError

# 로깅 설정
logging.basicConfig(filename="pybit.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

# API Key와 Secret 세팅
api_key = ""
api_secret = ""

# API 인증을 위한 HTTP 세션 생성
session = HTTP(
    testnet=False,
    api_key=api_key,
    api_secret=api_secret,
)

class BybitTradingBot:
    def __init__(self, session):
        self.session = session

    def get_market_price(self, symbol):
       

    def get_spot_balance(self, asset):
        

    def set_leverage(self, symbol, leverage=1):
        

    def xxxx(self, symbol, side):
        

    def xxxx(self, symbol, symbol):
        

    def xxxx(self, symbol, symbol):
       



def main():
    bot = BybitTradingBot(session)

    # 실행할 전략 선택
    choice = input()


    xxx = float(input())

    if choice == '1':
        bot.xxxx()
    elif choice == '2':
        bot.xxxx()
    else:
        print("잘못된 선택입니다. 1 또는 2를 입력하세요.")

if __name__ == "__main__":
    main()


# 설치 명령어
# pip install pybit
# 실행 명령어
# python 1_1번봇.py
