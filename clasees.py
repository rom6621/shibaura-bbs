#################################################
### Designer :開米大輝
### Date :2021.06.13
### Purpose :C1 UI処理部からの操作によって、書き込みを追加または削除するようC7 書込情報管理部を呼び出す。
#################################################

### Revision :
### V1.0 : 開米, 2021.06.13
### V1.1 : 開米, 2021.06.15 writeEntry, deleteEntry
### V1.2 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く
### V1.3 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く

#################################################
### Function Name :dealEntry
### Designer :開米大輝
### Date :2021.06.13
### Function:UI処理部からの操作によって、書き込みを追加または削除するようC7 書込情報管理部を呼び出す。
### Return :
#################################################

import thread
import manageEntry

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
        return new

class Entry:
    id: int #書込の順番
    auther: str
    content: str

    def __init__(self, entryId, entryAuther, entryContent):
        self.id = entryId
        self.auther = entryAuther
        self.content = entryContent

    def exchangeContent(self):
        self.content = '削除されました'
        return self

class User:
    id: str
    mailAddress: str
    
    def __init__(self, userId, userMailAddress):
        self.id = userId
        self.mailAddress = userMailAddress

#書込みを登録する関数
def writeEntry(thread, entryAuther, entryContent):
    newEntry = thread.addEntry(entryAuther, entryContent)
    #addEntryで作成されたnewインスタンスを用いて関数を呼び出す
    newThread = addContents(new, thread)
    return newThread

#書込みを削除する関数
def deleteEntry(thread, entry):
    #書き込み内容のみを置き換えたものをnewインスタンスに入れる
    newEntry = entry.exchangeContent()
    newThread = deleteContents(new, thread)
    return newThread
