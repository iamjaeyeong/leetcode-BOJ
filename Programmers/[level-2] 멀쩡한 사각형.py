def solution(w,h):
    answer = 0
    def GCD(a, b):
        if b==0:
            return a
        return GCD(b, a%b)
    
    if w<h:
        gcd = GCD(h, w)
    else:
        gcd = GCD(w, h)
    if w>h:
        gradient = w/h
        unit = h
    else:
        gradient = h/w
        unit = w
    area = w*h
    w = w // gcd
    h = h // gcd
    unit = unit // gcd
    prev = 0
    sliced = 0
    for x in range(unit):
        y = (prev + gradient) + 1e-8
        int_y = int(y)
        prev = y - int_y
        sliced += int_y + 1
        
    return area - gcd*(sliced-1)
    
    
    