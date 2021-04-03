# This solution worked for accuracy, however failed for efficiency.


def solution(prices):
    answer = []
    
    prices.reverse()
    for i in range(0, len(prices)):
        answer.append(i)     # answer initialization
        
    for i in range(0, len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<prices[j] and answer[j]>j-i:
                answer[j] = j-i
                
                
    answer.reverse()
    return answer