def print_statistics(a_list):
    def mean(l):
        return sum(l)/len(l)

    def median(l):
        l.sort()
        middle = len(l)//2
        if len(l)%2 == 0:
            return (l[middle]+l[middle+1])/2
        else:
            return l[middle+1]
            
    def mode(l):
        count = {}
        results = []
        for elm in l:
            if elm in count:
                count[elm] += 1
            else:
                count[elm] = 1
        max_mode = max(count.values())
        for k,v in count.items():
            if v == max_mode:
                results += [k]
        return results
        # extra work to handle multiple modes
    
    #separate work into simplified functions
    print("Mean: " + str(mean(a_list)) + "\n")
    print("Median: " + str(median(a_list)) + "\n")
    print("Mode(s): " + str(mode(a_list)) + "\n")


