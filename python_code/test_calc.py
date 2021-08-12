# 获取测试数据
import pytest
import yaml

from python_code.Calculator import Calculator


def get_data():
    with open("./data.yaml") as f:
        datas = yaml.safe_load(f)
        return datas

#验证测试数据
def test_get_data():
    print(get_data())

#进行参数化测试
class Test_calc(object):

    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,except_result',get_data()["add"]["success"]["parametervalue"],ids=get_data()["add"]["success"]["ids"])
    def test_add_success(self, a, b, except_result):
        assert except_result == round(self.calc.add(a,b),2)
        print(except_result)

    @pytest.mark.div
    @pytest.mark.parametrize('a,b',get_data()["add"]["fail"]["parametervalues"],ids=get_data()["add"]["fail"]["ids"])
    def test_add_fail(self,a,b):
        with pytest.raises(ValueError) as e:
            values = self.calc.add(float(a),float(b))
            #result = self.calc.add(a, b)
            print(values)
            assert e.type == ValueError








