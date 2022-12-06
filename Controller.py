import httplib2
import os.path
import threading
from PyQt5 import QtGui
from model import QueryGenerator


class MainController:
    def __init__(self, ui):
        self.ui = ui
        self.queryGen = QueryGenerator()
        self.oblastDict = self.queryGen.get_oblast()
        self.peopleDict = {}

    def adjust_mainWindow(self):
        oblastNames = self.oblastDict.keys()
        self.ui.oblastComboBox.addItems(oblastNames)
        self.ui.oblastComboBox.activated.connect(lambda: self.update_table(self.ui.oblastComboBox.currentText()))
        self.ui.listPeople.clicked.connect(lambda: self.show_info(self.ui.listPeople.currentItem().text()))

    def update_table(self, oblast):
        date1 = self.ui.dateEdit_bottom.text().split(".")
        date1.reverse()
        date1 = "-".join(date1)

        date2 = self.ui.dateEdit_top.text().split(".")
        date2.reverse()
        date2 = "-".join(date2)

        self.ui.listPeople.clear()
        self.peopleDict = self.queryGen.get_people(self.oblastDict[oblast], date1, date2)
        self.ui.listPeople.addItems(self.peopleDict)

    def show_info(self, person):
        functions = [self.show_image, self.show_description, self.show_name,
                     self.show_birthDate, self.show_deathDate, self.show_link]

        for func in functions:
            func(person)

    def show_image(self, person):
        image = self.queryGen.get_image("dbr:" + person)
        if "image" in image[0]:
            uri_image = image[0]["image"]["value"]

            if not(os.path.exists(f'img\{person}.jpg')):
                h = httplib2.Http('.cache')
                response, content = h.request(uri_image)
                out = open(f'img\{person}.jpg', 'wb')
                out.write(content)
                out.close()

            pixmap = QtGui.QPixmap(f"img/{person}.jpg")
        else:
            pixmap = QtGui.QPixmap("img/user.png")
        self.ui.image_label.setPixmap(pixmap)

    def show_description(self, person):
        description = self.queryGen.get_description("dbr:" + person)
        if "description" in description[0]:
            res = set()
            for item in description:
                res.add(item["description"]["value"])
            self.ui.description_label.setText("\n".join(res))
        else:
            self.ui.description_label.setText("---")

    def show_name(self, person):
        name = self.queryGen.get_name("dbr:" + person)
        if "name" in name[0]:
            res = set()
            for item in name:
                if item != "":
                    res.add(item["name"]["value"])
            self.ui.name_label.setText("\n".join(res))
        else:
            self.ui.name_label.setText("---")

    def show_birthDate(self, person):
        birthDate = self.queryGen.get_birth_date("dbr:" + person)
        if "birthDate" in birthDate[0]:
            res = set()
            for item in birthDate:
                res.add(item["birthDate"]["value"])
            self.ui.birthYear_label.setText("\n".join(res))
        else:
            self.ui.birthYear_label.setText("---")

    def show_deathDate(self, person):
        deathDate = self.queryGen.get_death_date("dbr:" + person)
        if "deathDate" in deathDate[0]:
            res = set()
            for item in deathDate:
                res.add(item["deathDate"]["value"])
            self.ui.deathYear_label.setText("\n".join(res))
        else:
            self.ui.deathYear_label.setText("---")

    def show_link(self, person):
        link = self.queryGen.get_link("dbr:" + person)
        if "link" in link[0]:
            res = set()
            for item in link:
                res.add(item["link"]["value"])
            self.ui.link_label.setText("\n".join(res))
        else:
            self.ui.link_label.setText("---")