import os

# 记录所有的名片字典
card_list = []


def show_one_card(one_card):
    """
    该函数负责将一张名片的信息以表格的形式展示出来。先打印表格的标题，
    然后打印分隔线，最后打印具体的名片信息。

    参数:
    one_card (dict): 一个包含名片信息的字典，包括姓名、电话、QQ和邮箱。

    返回:
    无
    """
    # 打印名片的标题
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print()

    # 打印分隔线
    print("-" * 100)

    # 打印具体的名片信息
    print("%s\t\t%s\t\t%s\t\t%s" %
          (one_card["name"], one_card["phone"], one_card["qq"], one_card["email"]))

    # 打印分隔线
    print("-" * 100)


def show_menu(file_path="huanying.txt"):
    """
    显示菜单或欢迎信息。

    该函数尝试打开并读取指定的文本文件内容，通常用于显示菜单或欢迎信息。
    如果文件不存在或读取时发生错误，将打印相应的错误信息。

    参数:
    file_path(str): 文件名，默认为"huanying.txt"。这是要读取的文件的名称。

    返回值:
    无。该函数仅用于打印信息到控制台。
    """
    # 构建完整的文件路径
    full_path = os.path.join(os.getcwd(), file_path)

    try:
        # 打开并读取文件内容
        with open(full_path, "r", encoding='utf-8') as welcome_file:
            content = welcome_file.read()
            print(content)
    except FileNotFoundError:
        # 当文件未找到时，提示用户
        print("文件未找到，请检查文件路径是否正确。")
    except OSError as e:  # 捕获文件操作相关的异常
        # 当文件读取操作发生错误时，提示用户
        print(f"读取文件时发生错误：{e}")
    except Exception as e:  # 通用异常捕获
        # 当发生未知错误时，提示用户
        print(f"未知错误：{e}")


def new_card():
    '''
    新建名片
    '''
    # 输入详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ号码：")
    email_str = input("请输入电子邮箱：")
    # 根据信息建立字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 字典加入列表
    card_list.append(card_dict)

    print("-" * 50)
    print(card_list)
    print("添加 %s 名片成功！" % name_str)


def show_all():
    '''显示所有名片'''
    if len(card_list) == 0:
        print("当前没有任何的名片记录,请使用新增功能添加名片。")
    else:
        # 打印表头
        for name in ["姓名", "电话", "QQ", "邮箱"]:
            print(name, end="\t\t\t\t")
        print()
        print("-" * 100)
        for card_dict in card_list:
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s" %
                  (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
        print("-" * 100)


def search_card():
    '''搜索名片'''
    find_name = input("请输入你要寻找的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了")
            show_one_card(card_dict)
            break
    else:
        print("没有找到%s" % find_name)


def delete_card():
    delete_name = input("请输入你要删除名片的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == delete_name:
            print("找到了该名片")
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print()
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" %
                  (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            card_list.remove(card_dict)
            print("完成删除工作！")
            break
    else:
        print("没有找到%s，无法完成删除工作" % delete_name)


def input_card_info(dict_value, tip_message):
    """
    该函数提示用户输入一个新的名片信息，并检查该输入是否有效。
    如果用户输入非空字符串，则返回用户的新输入；否则，返回原有的字典值。

    参数:
    - dict_value: 原有的字典值，用于回退情况
    - tip_message: 字符串，提示用户输入信息的提示信息

    返回:
    - result_str: 字符串，如果用户有输入则为用户的输入，否则为原有的字典值
    """
    result_str = input(tip_message)  # 提示用户输入信息
    if len(result_str) > 0:  # 检查用户是否有输入信息
        return result_str  # 用户有输入，返回用户输入的信息
    else:
        return dict_value  # 用户没有输入，返回原有的字典值


def modify_card():
    '''修改名片'''
    modify_name = input("请输入你要修改名片的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == modify_name:
            # 显示一下原始名片
            print("找到了该名片，该名片原始记录是如下：")
            show_one_card(card_dict)

            # 进行名片的修改
            card_dict["name"] = input_card_info(card_dict["name"], "请输入新的姓名")
            card_dict["phone"] = input_card_info(
                card_dict["phone"], "请输入新的电话：")
            card_dict["qq"] = input_card_info(card_dict["qq"], "请输入新的QQ号码：")
            card_dict["email"] = input_card_info(
                card_dict["email"], "请输入新的电子邮箱：")
            print("完成修改工作！")

            # 展示修订后的名片
            print("修改后的名片如下：")
            show_one_card(card_dict)
            # 跳出循环
            break
    else:
        print("没有找到%s，无法完成修改工作" % modify_name)


def exit_card():
    '''退出系统'''
    pass


if __name__ == "__main__":
    show_menu()
