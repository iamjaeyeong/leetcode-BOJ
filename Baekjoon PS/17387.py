x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

x_overlapped = [max(min(x1, x2), min(x3, x4)), min(max(x1, x2), max(x3, x4))]
y_overlapped = [max(min(y1, y2), min(y3, y4)), min(max(y1, y2), max(y3, y4))]
error = 1e-3

if x1==x2 and x3==x4:
    if x_overlapped[0]==x_overlapped[1] and y_overlapped[1]>=y_overlapped[0]:
        answer = 1
    else:
        answer = 0
elif x1==x2:
    l2_grad = (y4 - y3) / (x4 - x3)
    l2_inter = y3 - l2_grad * x3
    x_pos = x1
    y_pos = l2_grad * x1 + l2_inter
    if x_overlapped[0]-error<=x_pos<=x_overlapped[1]+error and y_overlapped[0]-error<=y_pos<=y_overlapped[1]+error:
        answer = 1
    else:
        answer = 0
elif x3==x4:
    l1_grad = (y2 - y1) / (x2 - x1)
    l1_inter = y1 - l1_grad * x1
    x_pos = x3
    y_pos = l1_grad * x3 + l1_inter
    if x_overlapped[0]-error<=x_pos<=x_overlapped[1]+error and y_overlapped[0]-error<=y_pos<=y_overlapped[1]+error:
        answer = 1
    else:
        answer = 0
else:
    l1_grad = (y2 - y1) / (x2 - x1)
    l2_grad = (y4 - y3) / (x4 - x3)

    l1_inter = y1 - l1_grad * x1
    l2_inter = y3 - l2_grad * x3

    if l1_grad==l2_grad:
        if l1_inter!=l2_inter:
            answer = 0
        else:
            if x_overlapped[0]>x_overlapped[1]:
                answer = 0
            else:
                answer = 1    
    else:
        x_meet = (l2_inter - l1_inter) / (l1_grad - l2_grad)
        # y_meet = x_meet * l1_grad + l1_inter
        if x_overlapped[0]>x_overlapped[1]:
            answer = 0
        else:
            if x_overlapped[0]-error<=x_meet<=x_overlapped[1]+error:
                answer = 1
            else:
                answer = 0
            
print(answer)