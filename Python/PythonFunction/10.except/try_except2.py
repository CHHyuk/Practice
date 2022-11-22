def safe_pop_print(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3],5)

def safe_pop_print(list,index):
    if index<len(list): # 만약 인덱스가 리스트의 길이보다 작으면 출력
        print(list.pop(index))
    else: # 그렇지 않으면(인덱스가 리스트 길이보다 같거나 크면
        print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3],5)

try:
    import my_module
except ImportError:
    print("모듈이 없습니다.")