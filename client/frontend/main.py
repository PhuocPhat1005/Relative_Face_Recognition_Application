from PyQt6 import QtCore, QtWidgets, QtQuick
import sys
import home_page, signup_ui, login_ui, menu, found_users, user_info, credit_ui, check_login, check_upload_pic, check_signup, cities_districts_wards
import os

# processing ui
ui = ""
app = QtWidgets.QApplication(sys.argv)
Mainwindow = QtWidgets.QMainWindow()


def home_page_ui():
    global ui
    ui = home_page.Ui_Home_Page()
    ui.setupUi(Mainwindow)
    ui.signup_button.clicked.connect(signup_ui_load)
    ui.signin_button.clicked.connect(login_ui_load)
    ui.credit_button.clicked.connect(credit_ui_load)
    ui.exit_button.clicked.connect(Mainwindow.close)
    Mainwindow.show()


def signup_ui_load():
    global ui
    ui = signup_ui.Ui_Sign_Up_Page()
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(home_page_ui)
    ui.apply_button.clicked.connect(login_ui_load)
    Mainwindow.show()


def login_ui_load():
    global ui
    ui = login_ui.Ui_Sign_In_Page()
    ui.setupUi(Mainwindow)
    ui.cancel_button.clicked.connect(home_page_ui)
    ui.apply_button.clicked.connect(main_win_ui)
    ui.signup_button.clicked.connect(signup_ui_load)
    Mainwindow.show()


def credit_ui_load():
    global ui
    ui = credit_ui.Ui_Credit_Page()
    ui.setupUi(Mainwindow)
    ui.back_button.clicked.connect(home_page_ui)
    Mainwindow.show()


def main_win_ui():
    global ui
    ui = menu.Ui_Specific_Task()
    ui.setupUi(Mainwindow)
    ui.user_info_box.clicked.connect(user_info_ui)
    ui.found_user_box.clicked.connect(found_users_ui)
    ui.history_finding.clicked.connect(history_finding_ui)
    ui.return_home_page.clicked.connect(home_page_ui)
    Mainwindow.show()


def history_finding_ui():
    pass


def get_response_upload_pic():
    file_filter = "Image File (*.png *.jpg)"
    response = QtWidgets.QFileDialog.getOpenFileName(
        parent=Mainwindow,
        caption="Select a file",
        directory=os.getcwd(),
        filter=file_filter,
        initialFilter="Image File (*.png *.jpg)",
    )
    return response


def launch_upload_pic_ui(response=None):
    response = get_response_upload_pic()
    dlg = QtWidgets.QDialog()
    ui = check_upload_pic.Ui_Dialog()
    ui.setupUi(dlg)
    ui.exit_box.accepted.connect(dlg.accept)
    ui.exit_box.rejected.connect(dlg.reject)
    if response[0] != "":
        dlg.exec()


def user_info_ui():
    global ui
    ui = user_info.Ui_Info_Users_Page()
    ui.setupUi(Mainwindow)
    ui.download_pic.clicked.connect(launch_upload_pic_ui)
    ui.cancel_button.clicked.connect(main_win_ui)
    ui.location_app = cities_districts_wards.LocationApp(
        ui.nation_box, ui.city_box, ui.district_box, ui.ward_box
    )
    Mainwindow.show()


def found_users_ui():
    global ui
    ui = found_users.Ui_Found_Users_Page()
    ui.setupUi(Mainwindow)
    ui.pushButton.clicked.connect(launch_upload_pic_ui)
    ui.cancel_button.clicked.connect(main_win_ui)
    ui.location_app = cities_districts_wards.LocationApp(
        ui.nation_box, ui.city_box, ui.district_box, ui.ward_box
    )
    Mainwindow.show()


home_page_ui()
sys.exit(app.exec())
