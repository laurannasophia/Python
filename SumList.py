def sumItAll():
    numbers = input("Syötä haluamasi määrä lukuja välilyönnillä eroteltuina ")
    num_list = []
    num_list = numbers.split()
    num_list = [int(i) for i in num_list]
    result = sum(num_list)
    return print(result)

sumItAll()