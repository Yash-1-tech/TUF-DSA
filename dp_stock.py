def dp(arr):
    buy = 0
    sell = None
    for i in range(len(arr)):
        if arr[i] < arr[buy]:
            buy = i
            sell = i+1
        if i>buy and arr[i] > arr[sell]:
            sell = i
    return buy, sell

arr = [7,1,5,3,6,4]
buy_date, sell_date = dp(arr)
print(f"Buy on day {buy_date+1} @ {arr[buy_date]} and Sell on day {sell_date+1} @ {arr[sell_date]}" )

