class Entry:
    def __init__(self, entry_id, entry_auther, entry_content):
        self.id = entry_id
        self.auther = entry_auther
        self.content = entry_content

class Thread:
    def __init__(self, thread_id, thread_name, thread_details):
        self.id = thread_id
        self.name = thread_name
        self.details = thread_details
        self.last_entry_id = 0
        self.entries = []

    def addEntry(self, entry_auther, entry_content):
        self.last_entry_id += 1
        new = Entry(self.last_entry_id, entry_auther, entry_content)
        self.entries.append(new)

