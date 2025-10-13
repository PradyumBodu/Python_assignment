per = int(input('Enter Persantage : '))

if per>90 and per<=100:
    print('Grade A')
elif per>70 and per<=90:
    print('Grade B')
elif per>50 and per<=70:
    print('Grade C')
elif per>30 and per<=50:
    print('Grade D')
else:
    print('Grade E')