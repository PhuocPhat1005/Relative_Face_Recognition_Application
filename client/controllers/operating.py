import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
import json


class LocationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Dropdowns")
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()

        self.province_combo = QComboBox(self)
        self.district_combo = QComboBox(self)
        self.ward_combo = QComboBox(self)

        self.load_data()

        layout.addWidget(self.province_combo)
        layout.addWidget(self.district_combo)
        layout.addWidget(self.ward_combo)

        self.setLayout(layout)

        # Connect signals to slots
        self.province_combo.currentIndexChanged.connect(self.update_districts)
        self.district_combo.currentIndexChanged.connect(self.update_wards)

    def load_data(self):
        with open("tree.json", encoding="utf-8") as f:
            self.data = json.load(f)

        provinces = [
            province["name_with_type"]
            for province in self.data.values()
            if province["type"] == "thanh-pho" or province["type"] == "tinh"
        ]
        self.province_combo.addItems(provinces)

        self.update_districts()

    def update_districts(self):
        selected_province = self.province_combo.currentText()
        districts = [
            district["name_with_type"]
            for province in self.data.values()
            if province["name_with_type"] == selected_province
            for district in province.get("quan-huyen", {}).values()
        ]
        self.district_combo.clear()
        self.district_combo.addItems(districts)
        self.update_wards()

    def update_wards(self):
        selected_district = self.district_combo.currentText()
        wards = [
            ward["name_with_type"]
            for province in self.data.values()
            for district in province.get("quan-huyen", {}).values()
            if district["name_with_type"] == selected_district
            for ward in district.get("xa-phuong", {}).values()
        ]
        self.ward_combo.clear()
        self.ward_combo.addItems(wards)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LocationApp()
    window.show()
    sys.exit(app.exec())
