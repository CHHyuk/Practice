list = [1,2,3,4,5]
dict = ['one':1,'two':2]


"""
공통점
	    List	              Dictionary
생성	list = [ 1, 2 ,3 ]	/ dict = { 'one':1, 'two':2 }
호출	list[ 0 ]	        / dict[ 'one' ]
삭제	del( list[ 0 ] )	/ del( dict[ 'one' ] )
개수 확인	len( list )	    / len( dict )
값 확인	2 in list	        / 'two' in dict.keys( )
전부 삭제	list.clear( )	/ dict.clear( )

차이점
        List	                                              Dictionary
순서	삭제 시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다	/ key로 값을 가져오기 때문에 삭제 여부와 상관없다
결합	list1 + list2	                                    / dict1.update( dict2 )

"""