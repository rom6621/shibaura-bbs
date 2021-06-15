class Entry:
    id: int #書込の順番
    auther: str
    content: str

    def __init__(self, entryId, entryAuther, entryContent):
        self.id = entryId
        self.auther = entryAuther
        self.content = entryContent

    def deleteEntry(self):
        self.content = '削除されました'

class Thread:
    id: int
    name: str
    details: str
    lastEntryId: int
    entries = []

    def __init__(self, threadId, threadName, threadDetails):
        self.id = threadId
        self.name = threadName
        self.details = threadDetails
        self.lastEntryId = 0

    def addEntry(self, entryAuther, entryContent):
        self.lastEntryId += 1
        new = Entry(self.lastEntryId, entryAuther, entryContent)
        self.entries.append(new)
