import math

def distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def closest_pair(p):
    n=len(p)
    mindist=float("inf") #초기값을 양의 무한대로 할당
    for i in range(n-1):
        for j in range(i+1,n):
            dist=distance(p[i],p[j])
            if dist<mindist:
                mindist=dist
    return mindist

n=int(input())
p=[]
for i in range(n):
    x,y=tuple(map(int,input().split()))
    p.append((x,y))


print("최근접 거리:", closest_pair(p))