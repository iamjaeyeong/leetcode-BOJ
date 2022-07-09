def solution(new_id):
    # first step
    new_id = new_id.lower()
    
    #second step
    ch = ['.', '-', '_']
    new_id2 = ""
    for i in range(len(new_id)):
        ascii = ord(new_id[i])
        if 97<=ascii<=122 or 48<=ascii<=57 or new_id[i] in ch:
            new_id2 += new_id[i]
    
    #third step
    prev = 0
    new_id3 = ""
    for i in range(len(new_id2)):
        if new_id2[i]=='.':
            if prev:
                continue
            else:
                prev = 1
                new_id3 += new_id2[i]
        else:
            prev = 0
            new_id3 += new_id2[i]
            
    #fourth step
    new_id3 = new_id3.strip('.')
    
    #fifth step
    if len(new_id3)==0:
        new_id3 = 'a'
    
    #sixth step
    if len(new_id3)>=16:
        new_id3 = new_id3[:15].strip('.')
    
    #last step
    while len(new_id3)<3:
        new_id3 += new_id3[-1]
    return new_id3