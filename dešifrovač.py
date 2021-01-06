#############################
#     ŠIFROVÁNÍ NA SÍLU     #
#############################
šifra = "IVKJXVOFPWTGVDIAJMHVXZOVDIAJMHVXZWTGJPWJCVOVDIAJMHVXZWTGVWPCOJWTGJIVKJXVOFPPWJCVQNZXCIJKJQNOVGJNFMUZIDVWZUIDIZKJQNOVGJIDXXJEZNOQIDWTGUDQJOVUDQJOWTGNQZOGJGDYDOJNQZOGJQZOHZNQDODVOHVEZIZKJCGODGVJYWJCVWTGKJNGVIXGJQZFEHZIZHEVIOZIKMDNZGKMJOJVWTQTYVGNQZYZXOQDJOJHNQZOGZVWTQNDXCIDPQZMDGDNFMUZIZCJEVINVHIZWTGODHNQZOGZHVGZKMDNZGVWTJOJHNQZOGZQTYVGNQZYZXOQDWTGJOPKMVQZNQZOGJFOZMZJNQZXPEZFVUYZCJXGJQZFVOJKMDXCVUZGJYJNQZOVIVNQZOZWTGNQZONFMUZIZEKJQNOVGVGZNQZOCJIZKJUIVGKMDNZGYJNQZCJQGVNOIDCJVGZEZCJQGVNOIDCJIZKMDEVGDOZHKVFFOZMDCJKMDEVGDVQZMDQEZCJEHZIJYVGHJXNOVONZWJUDHDYZOHD"
#šifra = input("Vložte šifru:   ")
písmena = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for klíč in range(len(písmena)):
    dešifrování = ''
    for symbol in šifra:
        if symbol in písmena:
            num = písmena.find(symbol)
            num = num - klíč
            if num < 0:
                num = num + len(písmena)
            dešifrování = dešifrování + písmena[num]
        else:
            dešifrování = dešifrování + symbol
    print('Klíč #%s: %s' % (klíč, dešifrování))
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")