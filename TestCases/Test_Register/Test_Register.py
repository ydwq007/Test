# -*- coding: utf-8 -*-
"""
接口：
创建人：魏奇
创建时间：2021-04-07 18:00
描述：
"""

import Excel, Plan, unittest,json,logging
import config, Basic_Interface, Excel_Manage

file_path = config.file_path  # 用例文件
sheet_name = "register"  # 用例表名
test_url = config.test_url_mall  # 用例域名

class register(Plan.Plan):

    def register_DataPreparation(self, file_path, sheet_name, value):
        """注册数据准备"""
        try:
            # 获取用例所在位置
            # filepath = "../TestDatas/云服务_接口测试用例-魏奇.xlsx"
            # sheetname = "register"
            # value = "test_register_001"
            data_position = Excel_Manage.Excel_DataPosition()
            data_position.excel_dataposition(file_path, sheet_name, value)
            row = data_position.excel_dataposition(file_path, sheet_name, value)[0]

            # 获取注册手机号
            excel_xl = Excel_Manage.excelprocess_xl()
            pre_parameter = json.loads(excel_xl.read_excel_xls(file_path, sheet_name, 2, row, 5))
            sms_mobile = pre_parameter["sms_mobile"]
            regi_mobile = pre_parameter["regi_mobile"]
            imgcode = pre_parameter["imgCode"]
            randcode = pre_parameter["randcode"]
            codeKey = pre_parameter["codeKey"]

            # 获取注册短信验证码
            captcha = Basic_Interface.get_captcha_image(test_url, config.headers)
            codekey_1 = captcha[0]
            sms_data = {
                "account": sms_mobile,
                "business": "REGISTER",
                "channel": "SMS",
                "imgCode": "54",
                "imgCodeKey": codekey_1
            }
            auth_code = Basic_Interface.get_SmsCode(test_url, config.headers, sms_data)

            if imgcode == "null":
                new_imgcode = ""
            elif len(imgcode) == 0:
                new_imgcode = 54
            else:
                new_imgcode = imgcode

            if randcode == "null":
                new_randcode = ""
            elif len(randcode) == 0:
                new_randcode = auth_code
            else:
                new_randcode = randcode

            if codeKey == "null":
                new_codeKey = ""
            elif len(codeKey) == 0:
                new_codeKey = codekey_1
            else:
                new_codeKey = codeKey

            # if bool(imgcode) == False:
            #     imgcode = 54
            # if bool(randcode) == False:
            #     randcode = auth_code
            # if bool(codeKey) == False:
            #     codeKey = codekey_1

            # 组装注册参数
            interface_parameters = {
                "busOrgId": "",
                "codeKey": new_codeKey,
                "imgCode": new_imgcode,
                "invStyle": "",
                "invType": "",
                "invUid": "",
                "mobile": regi_mobile,
                "orgId": "",
                "randcode": new_randcode
            }
            interface_parameters_new = json.dumps(interface_parameters)

            # 更新用例参数
            excel_xl.write_excel_xls_modify(file_path, row, 9, interface_parameters_new, sheet_name=sheet_name, style=1)
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n注册数据准备结束")


    def test_register_001(self):
        """新手机号注册成功"""

        try:
            case_no = "test_register_001"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_002(self):
        """手机号为空"""

        try:
            case_no = "test_register_002"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_003(self):
        """手机号输入类型错误"""

        try:
            case_no = "test_register_003"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_004(self):
        """手机号长度超过11位"""

        try:
            case_no = "test_register_004"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_005(self):
        """手机号长度小于11位"""

        try:
            case_no = "test_register_005"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_006(self):
        """手机号已注册"""

        try:
            case_no = "test_register_006"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_007(self):
        """手机验证码错误"""

        try:
            case_no = "test_register_007"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_008(self):
        """手机验证码失效"""

        try:
            case_no = "test_register_008"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_009(self):
        """图形验证码为空"""

        try:
            case_no = "test_register_009"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_010(self):
        """图形验证码失效"""

        try:
            case_no = "test_register_010"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_011(self):
        """图形验证码计算错误"""

        try:
            case_no = "test_register_011"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

    def test_register_012(self):
        """手机验证码为空"""

        try:
            case_no = "test_register_012"
            self.register_DataPreparation(file_path, sheet_name, case_no)
            result = Excel.run_xlsx(file_path, sheet_name, case_no, test_url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")

if __name__ == "__main__":
    unittest.main()
