# -*- coding: utf-8 -*-
"""
接口：普通订单的创建
创建人：魏奇
更新人：魏奇
更新时间：2020-01-08 9:23
描述：
"""

import unittest,sys,json
sys.path.append("../../Commom")
import Excel,Plan,Excel_Manage,Data_Structure
sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall # mall地址
filepath = config.filepath # 用例文件
resheetname = "normal_order_create" # 用例表
# loginsheet = "login_moblie" # 用例表
loginurl = config.test_url_chome # 登录地址
Nomal_login_data = config.aloneA # 纯A账号
shop_login_data = config.dealer1 # 关联B账号
no_certificate_data = config.dealer2 # 无证书信息账号
err_certificate_data = config.dealer3 # 证书信息异常账号
no_dog_data = config.dealer4 # 无加密狗
currency_dog_data = config.dealer5 # 通狗
no_dealer_data = config.dealer6 # 无经销商
headers = config.headers # 登录信息头
normal_order = json.dumps(config.normal_order) # 普通订单

class Nomal_Order_Create(Plan.Plan):

    def test_normal_order_create_case_00(self):
        """登录更改Authorization"""
        try:
            # 登录
            Auserlogin = Data_Structure.get_token(loginurl,Nomal_login_data,headers) # A账号登录
            Buserlogin = Data_Structure.get_token(loginurl,shop_login_data,headers)# B账号登录
            Buserlogin01 = Data_Structure.get_token(loginurl,no_certificate_data,headers) # 无证书
            Buserlogin02 = Data_Structure.get_token(loginurl,err_certificate_data,headers) # 证书异常
            Buserlogin03 = Data_Structure.get_token(loginurl,no_dog_data,headers) # 未绑定加密狗
            Buserlogin04 = Data_Structure.get_token(loginurl,currency_dog_data,headers) # 通狗
            Buserlogin05 = Data_Structure.get_token(loginurl,no_dealer_data,headers) # 无经销商单位

            #更新数据
            mdvalue1 = Buserlogin[2]
            mdvalue2 = Auserlogin[2]
            mdvalue3 = Buserlogin01[2]
            mdvalue4 = Buserlogin02[2]
            mdvalue5 = Buserlogin03[2]
            mdvalue6 = Buserlogin04[2]
            mdvalue7 = Buserlogin05[2]
            excel_xl = Excel_Manage.excelprocess_xl()
            # 修改测试用例
            excel_xl.write_excel_xls_modify(filepath,18,5,mdvalue1,sheet_name=resheetname,style=3,original_row=5) # 修改第5行到17行的第5列的值(请求头)
            excel_xl.write_excel_xls_modify(filepath,7,6,normal_order,sheet_name=resheetname,style=3,original_row=4) # 修改第4行到5行的第6列的值(请求参数)
            excel_xl.write_excel_xls_modify(filepath,4,5,mdvalue2,sheet_name=resheetname,style=1) # 修改第4行第5列的值(请求头)
            excel_xl.write_excel_xls_modify(filepath,19,5,mdvalue3,sheet_name=resheetname,style=1) # 修改无证书(请求头)
            excel_xl.write_excel_xls_modify(filepath,20,5,mdvalue4,sheet_name=resheetname,style=1) # 修改证书异常(请求头)
            excel_xl.write_excel_xls_modify(filepath,21,5,mdvalue4,sheet_name=resheetname,style=1) # 修改无加密狗(请求头)
            excel_xl.write_excel_xls_modify(filepath,22,5,mdvalue4,sheet_name=resheetname,style=1) # 修改通狗(请求头)
            excel_xl.write_excel_xls_modify(filepath,23,5,mdvalue4,sheet_name=resheetname,style=1) # 修改无经销商(请求头)
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_01(self):
            """正常订单数据（含B类账号）"""
            try:
                file = Excel.open_xlsx(filepath)
                result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_01",Test_Url)
                self.assertEqual(True, result[0])
                # print(result)
                normal_order_id = result[1]["data"]["data"]["order_id"]
                return normal_order_id #返回创建成功的普通订单id
            except Exception as err:
                raise
            finally:
                print("调用接口结束")

    def test_normal_order_create_case_02(self):
        """用户未登录"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_02",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_03(self):
        """token失效"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_03",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_04(self):
        """user_id-非必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_04",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_05(self):
        """goods_sku_list-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_05",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_06(self):
        """goods_sku_list-商品不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_06",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_07(self):
        """buyer_org_id-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_07",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_08(self):
        """buyer_org_id-客户单位不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_08",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_09(self):
        """buyer_org_id-客户单位不匹配"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_09",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_10(self):
        """service_org_id-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_10",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_11(self):
        """service_org_id-经销商不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_11",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_12(self):
        """service_org_id-经销商不匹配"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_12",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_13(self):
        """company_name-必填"""
        # 这个场景有问题，没有校验必填
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_13",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_14(self):
        """contact_name-非必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_14",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_15(self):
        """contact_phone-必填"""
        # 这个场景有问题，没有校验必填
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_15",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_16(self):
        """正常订单数据（纯A类账号）"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_16",Test_Url)
            self.assertEqual(True, result[0])
            # print(result)
            normal_order_id = result[1]["data"]["data"]["order_id"]
            return normal_order_id #返回创建成功的普通订单id
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_17(self):
        """版本不匹配"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_17",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_18(self):
        """证书不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_18",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_19(self):
        """证书异常"""
        # 这个场景，不校验证书有效性，只判断证书是否存在
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_19",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_20(self):
        """未绑定狗号"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_20",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_21(self):
        """通狗下单"""
        # 这个场景有问题，通狗应该不能下单
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_21",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_normal_order_create_case_22(self):
        """无经销商单位"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_22",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")



if __name__ == "__main__":
    unittest.main()
