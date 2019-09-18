def compareVersion(v1, v2):
    iters = min(len(v1),len(v2))
    for i in range(iters):
        if int(v1[i]) > int(v2[i]):
            print("1")
            return
        elif int(v1[i]) < int(v2[i]):
            print("-1")
            return
    print("0")
versions = input().split(" ")
v1 = versions[0].split(".")
v2 = versions[1].split(".")
compareVersion(v1, v2)