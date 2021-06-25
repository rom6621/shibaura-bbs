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

    #引数から新しい書込を作る関数
    def addEntry(self, entryAuther, entryContent):
        self.lastEntryId += 1
        new = Entry(self.lastEntryId, entryAuther, entryContent)
        #作った書込をThreadクラスに格納する
        self.entries.append(new)
        #addEntryで作成されたnewEntryを用いて関数を呼び出す
        manageEntry.addContents(newEntry, self.id)

    #スレッドを呼び出す際に、entriesに関連した書込みを配列に入れる関数
    def getEntry(self):
        #new配列を初期化し、関数を呼び出し返り値をnew配列に代入していく
        new = []
        new = manageEntry.contentsProcessing(self.id)
        #受け取った配列を、Threadクラスのentries配列に代入していく
        for i in new:
            self.entries.append(i)
        #書込みの順番を更新する
        self.lastEntryId = len(self.entries)

    #書込みを削除する関数
    def deleteEntry(self, id):
        #渡されたidの書込の内容を書き換える
        self.entries[id].content = '削除されました'
        manageEntry.deleteContents(self.entries[id], self.id)

class Entry:
    id: int #書込の順番
    auther: str
    content: str

    def __init__(self, entryId, entryAuther, entryContent):
        self.id = entryId
        self.auther = entryAuther
        self.content = entryContent

class User:
    id: str
    mailAddress: str

    def __init__(self, userId, userMailAddress):
        self.id = userId
        self.mailAddress = userMailAddress

def addContents(a, b):
    s=0
