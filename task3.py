# TODO Найдите количество книг, которое можно разместить на дискете
a=100
b=50
c=25
d=4
sum=a*b*c*d
byaj=1.44*1024*1024
book=byaj/sum
#book=round(book,0)
book=int(book)



print("Количество книг, помещающихся на дискету:", book)
