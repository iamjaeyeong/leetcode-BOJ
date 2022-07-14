class Solution:
    def trap(self, height) -> int:
        ret = 0
        level = 0
        s = -1
        for i in range(1, len(height)):
            if height[i-1]<height[i]:
                continue
            else:
                s = i-1
                break
        if s==-1:
            return 0
        stack = [[height[s], s]]
        
        for i in range(s+1, len(height)):
            if height[i]<stack[-1][0]:
                stack.append([height[i], i])
                level = height[i]
            elif height[i]==stack[-1][0]:
                stack[-1][1] = i
            else:
                while 1:
                    temp = stack.pop()
                    if temp[0]>=height[i]:
                        ret += (height[i]-level)*(i-temp[1]-1)
                        level = height[i]
                        if temp[0]>height[i]:
                            stack.append(temp)
                        else:
                            stack.append([temp[0], i])
                        break
                    elif len(stack)==0:
                        ret += (temp[0]-level)*(i-temp[1]-1)
                        level = temp[0]
                        stack.append([height[i], i])
                        break
                    else:
                        ret += (temp[0]-level)*(i-temp[1]-1)
                        level = temp[0]
                stack.append([height[i], i])
        return ret
                        