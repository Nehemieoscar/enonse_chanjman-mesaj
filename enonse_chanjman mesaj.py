#pou mw arive realize enonse sa mw di tet mw ke premye sa ke mw ap gen bezwen se yon lis kote mw deklare tout let alfabet a
alfabet = ['A', 'B', 'cC', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

user = input("Antre yon mesaj kote ou ap itilize >reprezante yon deplasman adwat reprezante yon deplasman agoch:")

Kant_desplasman = [int(i)for i in user if i.isdigit()]
kantite = int(''.join(map(str,Kant_desplasman )))

if user[0] == ">":
    a=alfabet.index (user[2])
    pozisyon = (a + (kantite) )% len(alfabet)
    l=alfabet[pozisyon]
elif user[0] == "<":
    a=alfabet.index (user[2])
    pozisyon = (a - (kantite) )% len(alfabet)
    l=alfabet[pozisyon]
else :
    print("Ou gen yon bagay , ou mal mete nan mesaj ou antre a! Rantre yon lot mesaj ")
nouvo_mesaj += l
print("nouvo mesaj la se:",nouvo_mesaj )
