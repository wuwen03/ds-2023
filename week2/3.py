
mp=[[1],[0,2],[1,3,5],[2,4],[3,5,7],[2,4,6],[5,7],[4,6,8],[7,9],[8]]
name=["人羊狼菜","狼菜","人狼菜","狼","人羊狼","菜","人羊菜","羊","人羊","成功"]
ans=[]
vis=[0]*10
def dfs(now:int,fa:int)->None:
    # print(fa,"->",now)
    if now==9:
        print(ans)
        return
    # print(mp[now])
    for to in mp[now]:
        if vis[to]:
            continue
        ans.append(name[to])
        vis[to]=1
        dfs(to,now)
        vis[to]=0
        ans.pop()
ans.append(name[0])
dfs(0,-1)