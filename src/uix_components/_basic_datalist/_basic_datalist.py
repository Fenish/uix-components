import uix
from uix.elements import option, datalist, input

class basic_datalist(uix.Element):
    def __init__(self, name, value=None, id=None, options=[], callback=None):
        super().__init__(name, id=id)
        self.options = options
        self.datalistID = id + "-datalist"
        self.inputID = id + "-input"
        self.callback = callback
        self.cls("border")
        
        with self:
            input(value="", id=self.inputID, type="text", list=self.datalistID).on("change", self.on_dlist_change).style("margin-left", "10px;")
            with datalist(id=self.datalistID):
                for opt in self.options:
                    option(value=opt, id=opt)
            
    def on_dlist_change(self, ctx, id, value):
        if self.callback:
            self.callback(ctx, id, value)
        
title = "Basic Datalist"
description = """
# basic_datalist(name, value, id, options[], callback)
1. Input elementinin içerinde datalist elementi eklenerek oluşturulan bir componenttir. option elementi ile datalist'in içi doldurulur.
    | attr          | desc                                                          |
    | :------------ | :------------------------------------------------------------ |
    | name          | Datalist Componentinin name'i input'un önünde yazar           |
    | value         | Datalist Componentinin içeriği                                |
    | id            | Datalist Componentinin id'si                                  |
    | option        | Datalist Componentinin liste elemanlarını array olarak alır   |
    | callback      | Listeden bir seçim yapıldıığında çağırılacak fonksiyon        |
"""
sample = """
def basic_datalist_example():
    options = ["BMW","AUDI","MERCEDES"]
    return basic_datalist(name="Car List", id = "datalist", options = options, 
                          callback = lambda ctx, id, value: print(f"Datalist {id} changed to: {value}"))
"""