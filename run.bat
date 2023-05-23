 pytest -v -s --html=Reports\login_page.html TestCases/test_HRM_login_page.py --browser chrome
  pytest -v -s -m 'regression' --html=Reports\regression_group_test.html TestCases --browser firefox

rem pytest -v -s --html=Reports\home_page.html TestCases/test_HRM_home_page.py --browser chrome
rem pytest -v -s --html=Reports\login_page_ddt.html TestCases/test_HRM_login_page_ddt.py --browser chrome
rem pytest -v -s -m 'sanity' --html=Reports\sanity_group_test.html TestCases --browser chrome
