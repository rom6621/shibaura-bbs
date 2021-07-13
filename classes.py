#################################################
### Designer :開米大輝・浅瀬石遊那
### Date :2021.06.13
### Purpose :C1 UI処理部からの操作によって、書き込みを追加または削除するようC7 書込情報管理部を呼び出す。
#################################################

### Revision :
### V1.0 : 開米, 2021.06.13
### V1.1 : 開米, 2021.06.15 addEntry, deleteEntry追加
### V1.2 : 浅瀬石, 2021.06.25 ユーザ取得処理，ネーム更新処理 追加
### V1.3 : 開米, 2021.06.25 getThread, createThread追加


import thread
import manageThread
import manageEntry
import manageUsers

#スレッドのクラス
class Thread:
    id: int
    name: str
    details: str
    lastEntryId: int
    entries = []
    #スレッドID、スレッド名、詳細、書込み数、書込み

    def __init__(self, threadId, threadName, threadDetails, entries=[], lastId=0):
        self.id = threadId
        self.name = threadName
        self.details = threadDetails
        self.entries = entries
        self.lastEntryId = lastId

    def __str__(self):
        return str(self.id)

#################################################
### Function Name :getThread
### Designer :開米 大輝
### Date :2021.06.25
### Function:スレッドIDに紐づいたスレッド名とスレッド詳細と書込みを呼び出す処理
### Return :threadId-スレッドのID
###         threadName-スレッド名
###         threadDetails-スレッド詳細
###         entries-書込み
###         len(entries)-スレッドの書込数
#################################################

    @classmethod
    def getThread(cls, threadId):
        ret = manageThread.getThread(threadId)
        threadName = ret[1]
        threadDetails = ret[2]
        entries = manageEntry.contentsProcessing(threadId)
        return cls(threadId, threadName, threadDetails, entries, len(entries))

#################################################
### Function Name :createThread
### Designer :開米 大輝
### Date :2021.06.25
### Function:渡されたスレッド名と詳細から新しいスレッドを作成する処理
### Return :threadId-スレッドのID
###         threadName-スレッド名
###         threadDetails-スレッド詳細
#################################################

    @classmethod
    def createThread(cls, threadName, threadDetails):
        #管理部にスレッド名と詳細を送り、紐づいたIDを作ってもらう
        threadId = manageThread.threadRegistration(threadName, threadDetails)
        return cls(threadId, threadName, threadDetails)

#################################################
### Function Name :addEntry
### Designer :開米 大輝
### Date :2021.06.15
### Function:渡されたユーザ名と書込内容から新しいスレッドを作成する処理
### Return :lastEntryId-書込数
###         entryAuthor-利用者のユーザ名
###         entryContent-書込内容
#################################################

    def addEntry(self, entryAuthor, entryContent):
        self.lastEntryId += 1
        newEntry = Entry(self.lastEntryId, entryAuthor, entryContent)
        #作った書込をThreadクラスに格納する
        self.entries.append(newEntry)
        #addEntryで作成されたnewEntryを用いて関数を呼び出す
        manageEntry.addContents(newEntry, self.id)
        return newEntry

#################################################
### Function Name :deleteEntry
### Designer :開米 大輝
### Date :2021.06.15
### Function:IDに紐づいた書込みの内容を書き換える処理
### Return : なし
#################################################

    def deleteEntry(self, entryId):
        #渡されたidの書込の内容を書き換える
        self.entries[id-1].content = '削除されました'
        manageEntry.deleteContents(self.entries[id-1], self.id)

#書き込みクラス
class Entry:
    id: int
    content: str
    #書込みの順番、内容

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

#################################################
### Function Name :getUser
### Designer :浅瀬石 遊那
### Date :2021.06.25
### Function:ユーザIDに結び付いたメールアドレスとユーザネームを呼び出す処理．
### Return :userId-利用者のユーザID
###         userMailAddress-利用者のメールアドレス
###         userName-利用者のユーザネーム
#################################################

    @classmethod
    def getUser(cls, userId):
        ret = manageUsers.getUser(userId)
        mailAddress = ret[0]
        userName = ret[1]
        return cls(userId, mailAddress, userName)

#################################################
### Function Name :updateName
### Designer :浅瀬石 遊那
### Date :2021.06.25
### Function:ユーザネームを更新する関数を呼び出す処理．
### Return :なし
#################################################

def updateName(userId, name):
    manageUsers.userNameUpdate(userId, name)
