
def getGroups(keys):
    res = []
    done_index = []
    for i in range(len(keys)):
        if i not in done_index:
            # continue
            temp = []
            temp.append(keys[i])
            temp_key_1 = keys[i]
            for j in range(i+1,len(keys)):
                if j not in done_index:
                    temp_key_2 = keys[j]
                    if sorted(temp_key_1) == sorted(temp_key_2):
                        temp.append(keys[j])
                        done_index.append(j)
            res.append(temp)

    print(res)


if __name__ == "__main__":
    # here the below keys are just example, this can be taken in input
    keys = ["idea", "idae", "bsnl", "nsbl", "grasim", "bata"]
    getGroups(keys)
