def countingValleys(n, s):
    sum1=0
    index_cap=0
    index_array=[]
    count_valley=0
    for i in s :
        if i=="U":
           sum1+=1
           index_cap+=1
        elif i=="D":
            sum1-=1
            index_cap+=1
        if sum1==0:
            index_array.append(index_cap)
            i=index_array[-1]
            if s[i-1]=="U":
             count_valley+=1
    return(count_valley)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
