#################################################
### Designer : 鈴木一史
### Date : 2021/06/13
### Purpose : C1 UI処理部から渡された検索語句とタグをC6スレッド情報管理部に渡す
#################################################

#################################################
### Function Name : SearchProcessing
### Designer : 鈴木一史
### Date : 2021/06/13
### Function: C1 UI処理部から渡された検索語句とタグをC6スレッド情報管理部に渡す。
### Return : search_word,search_tag
#################################################
def SearchProcessing(String line):

    search_word = []
    search_tag = []

    #スペース文字で文字列を分解
    keywords = line.split(" ")

    #検索語句かタグかを判別
    for keyword in keywords:
        if(keyword[0] == "#"):
            search_tag.append(keyword[1:])
        else:
            search_word.append(keyword)

    #検索語句の配列とタグの配列をまとめる作業
    search_key = []
    search_key.append(search_word)
    search_key.append(search_tags)

    # search_key[ [検索語句1,検索語句2,...], [タグ1,タグ2,....]]
    return search_key
    