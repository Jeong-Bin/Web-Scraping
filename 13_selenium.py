# selenium : 웹 페이지의 테스트 자동화를 할 수 있는 프에임웤
# selenium을 통해 직접 웹 브라우저를 컨트롤 하면서 html문서를 가져오면 이후 BeautifulSoup을 통해서 스크래핑 할 수 있음

# pip install selenium

# 크롬 드라이버도 설치해줘야 함.
    # 1. 구글 우측 점3개 - 도움말 - 크롬 정보 - 버전 확인
    # 2. chromedriver 검색. 맨 위 사이트 - 자기 크롬 버전에 맞는 드라이버 설치
    # 3. 다운받은 파일을 사용할 워크스페이스로 가져온 뒤 압축을 푼다.

from selenium import webdriver

browser = webdriver.Chrome() # 만약 크롬드라이버가 다른 경로에 있다면 괄호 안에 경로를 ""로 적어줘야 함
browser.get("http://naver.com") # 크롬 웹드라이버 객체를 생성하고 그 브라우저에서 이 url로 이동함

# 이후에는 터미널에서 작업 함
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get("http://naver.com")
# elem = browser.find_element_by_class_name("link_login")  # 이름이 link_login인 element(로그인 버튼)
# elem
# elem.click()  # 로그인 버튼을 클릭함
# browser.back()  # 뒤로가기
# browser.forward()  # 앞으로 가기
# browser.refresh()  # 새로고침
# elem = browser.find_element_by_id("query")  # id가 query인 element (검색창)
# from selenium.webdriver.common.keys import Keys  #  Keys.ENTER를 사용하기 위해 임포트
# elem.send_keys("코딩")  # 검색창에 내용 입력
# elem.send_keys(Keys.ENTER)  # ENTER 키 입력