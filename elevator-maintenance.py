def solution(l):
    #this is meant to run in python 2.7.13 but it works in 3.7.4 as well
    # Your code here
    #turn each string into a list on integers and create a list of lists
    versionInts = sorted([[int(r) for r in version.split('.')] for version in l])

    reString = ['.'.join([str(r) for r in version]) for version in versionInts]
    
    #sortedVersions = ','.join(reString)
    #this wasn't actually necessary
    return reString

l1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
solution1 = "0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0"
l2 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
solution2 = "1.0,1.0.2,1.0.12,1.1.2,1.3.3"
answer = solution(l1)
print(answer)

