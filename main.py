
class TreeStore():
    def __init__(self, items):
        self.items = items

    def getAll(self):
        return self.items

    def getItem(self, id):
        for self.item in self.items:
            if self.item.get('id') == id:
                return self.item

    def getChildren(self, chil):
        result = []
        for self.item in self.items:
            if self.item.get('parent') == chil:
                result.append(str(self.item))
        return result

    def getAllParents(self, paren):  
        self.result = []
        self.z = paren
        while self.z != 'root':
            for self.item in self.items:
                if self.item.get('id') == self.z:
                    self.z = self.item.get('parent')
                    for self.it in self.items:
                        if self.it.get('id') == self.z:
                            self.result.append(str(self.it))
   
        return self.result
  
items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)


ts.getAll()
ts.getItem(7)
ts.getChildren(4)
ts.getAllParents(7)

# Примеры использования:
#  - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
#
#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#
#  - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]
