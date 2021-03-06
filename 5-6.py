python の　set について

set型 とは　python における集合を扱うための型である。

もっとも普及しているリスト型のように、set型も同じく複数の値を格納できる型である。

リスト型との違いは、重複した要素がない、要素に順番がないといった２点が挙げられる。

set型オブジェクトを作成するには

myset = set([1,2,3])
myset = set([1,2,3,3,2,1])
print(myset1)
print(myset2)

出力結果は
{1,2,3}
{1,2,3}
である。

上のコードでは３つの整数を含むset型オブジェクトを２つ作成し表示させたもの。

myset2は重複した要素を含むが、出力されるときは重複された要素は無視されるため、
両方とも同じ内容が表示された。