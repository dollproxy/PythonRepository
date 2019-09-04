#Sorting a integer list 
listInput = input("Write a integer list ")
numberList = [int(i) for i in listInput.split(",")]
numberList.sort()
print ('Sorted number list', numberList)

#Sorting a string list
stringInput = input("Write a string list ")
stringList = [str(i) for i in stringInput.split(",")]
stringList.sort()
print(stringList)