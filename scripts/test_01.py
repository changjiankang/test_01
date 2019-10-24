import allure
import pytest

class Test(object):
    @allure.step(title="练习01")
    def test_lianxi_01(self):
        allure.attach("失败原因", "密码错误")
        print('练习01')

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_lianxi_02(self):
        allure.attach("失败原因", "验证码错误")
        print("练习02")

    @allure.step(title="练习03")
    def test_lianxi_03(self):
        print("练习03")
