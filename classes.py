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
import manageThread
import manageEntry
import manageUsers

class Thread:
    id: int
    name: str
    details: str
    lastEntryId: int
    entries = []

    def __init__(self, threadId, threadName, threadDetails, entries=[], lastId=0):
        self.id = threadId
        self.name = threadName
        self.details = threadDetails
        self.entries = entries
        self.lastEntryId = lastId

    def __str__(self):
        return str(self.id)

    # スレッドIDからスレッドクラスを取得する
    @classmethod
    def getThread(cls, threadId):
        ret = manageThread.getThread(threadId)
        threadName = ret[1]
        threadDetails = ret[2]
        entries = manageEntry.contentsProcessing(threadId)
        return cls(threadId, threadName, threadDetails, entries, len(entries))

    @classmethod
    def createThread(cls, threadName, threadDetails):
        threadId = manageThread.threadRegistration(threadName, threadDetails)
        return cls(threadId, threadName, threadDetails)

    #引数から新しい書込を作るメソッド
    def addEntry(self, entryAuthor, entryContent):
        self.lastEntryId += 1
        newEntry = Entry(self.lastEntryId, entryAuthor, entryContent)
        #作った書込をThreadクラスに格納する
        self.entries.append(newEntry)
        #addEntryで作成されたnewEntryを用いて関数を呼び出す
        manageEntry.addContents(newEntry, self.id)
        return newEntry

    #書込みを削除するメソッド
    def deleteEntry(self, id):
        #渡されたidの書込の内容を書き換える
        self.entries[id-1].content = '削除されました'
        manageEntry.deleteContents(self.entries[id-1], self.id)

class Entry:
    id: int #書込の順番
    content: str

    def __init__(self, entryId, entryAuthor, entryContent):
        self.id = entryId
        self.author = entryAuthor
        self.content = entryContent

class User:
    id: str
    mailAddress: str
    name: str

    def __init__(self, userId, userMailAddress, userName):
        self.id = userId
        self.mailAddress = userMailAddress
        self.name = userName

    @classmethod
    def getUser(cls, userId):
        ret = manageUsers.getUser(userId)
        mailAddress = ret[0]
        userName = ret[1]
        return cls(userId, mailAddress, userName)

def updateName(userId, name):
    manageUsers.userNameUpdate(userId, name)
