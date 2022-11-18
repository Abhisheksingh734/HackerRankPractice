
# dict={}
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         d={name:score}
#         dict.update(d)
# print(dict)

# print(dict["Harry"])

if __name__ == '__main__':
    name_score=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score.append([name,score])
    sorted_score=sorted(list(set([x[1] for x in name_score])))
    secondLowest=sorted_score[1]
    final_list=[]
    for i in name_score:
        if i[1]==secondLowest:
            final_list.append(i[0])
    for i in sorted(final_list):
        print(i)
        
    
