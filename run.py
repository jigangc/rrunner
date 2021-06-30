import os
from rrunner.cli import main_run

if __name__ == "__main__":
    # 运行所有的接口
    # pytest.main(
    #     ["-s", "--html=" + REPORT_DIR + r"\report.html", "--alluredir=" + REPORT_DIR + r"\allure", "--clean-alluredir"])
    exit_code = main_run(["testcases\\test_letsbim.xlsx"])
    #os.system('allure generate report/allure -o report/allure-report --clean')

