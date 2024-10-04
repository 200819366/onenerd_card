import os
import card_tools

# 菜单选项列表
menu_items = ['退出系统', '新建名片', '显示全部', '查询名片', '删除名片', '修改名片']

# 主程序循环，直到用户选择退出
while True:
    # 显示菜单
    card_tools.show_menu()
    # 增加输入验证
    select_input = input("请输入要选择的功能：").strip()
    # 检查输入是否为数字，并且在有效功能选项范围内
    try:
        if select_input.isdigit() and len(select_input) == 1 and\
                int(select_input) in range(len(menu_items)):
            # 根据用户选择调用相应的功能函数
            if select_input == "1":
                card_tools.new_card()
            elif select_input == "2":
                card_tools.show_all()
            elif select_input == "3":
                card_tools.search_card()
            elif select_input == "4":
                card_tools.delete_card()
            elif select_input == "5":
                card_tools.modify_card()
            elif select_input == "0":
                # 用户选择退出，打印告别语并跳出循环
                print("欢迎再次使用【名片管理系统 独饮版】")
                break
        else:
            # 输入验证失败，提示用户重新输入
            print("输入错误，请重新输入。")
    except ValueError:
        # 处理非数字输入的情况
        print("输入错误，请输入一个数字。")
    except Exception as e:
        # 其他异常处理，打印错误信息
        print(f"发生错误：{e}")
