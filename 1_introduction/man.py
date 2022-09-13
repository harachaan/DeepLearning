# 簡単なクラス作成の例

class Man:
    def __init__(self, name):  # selfってJavaScriptでいうthis的な扱い？
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")


m = Man("Harachan")
m.hello()
m.goodbye()

'''
ここでは，Man という新しいクラスを定義している．
上の例では，このMan というクラスから，m というインスタンス（オブジェクト）生成する．

Man クラスのコンストラクタ（初期化メソッド）は，nameという引数をとり，その引数でインスタンス変数であるself.nameを初期化する

インスタンス変数とは，個々のインスタンスに格納される変数のこと．

pythonでは，self.nameのように，selfの後に属性名を書くことで，インスタンス変数の作成およびアクセスができるようになる

インスタンスってなんやねん！！
'''
