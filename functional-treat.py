print("---Welcome To The Data Analyzer And Transformer Program---")
data_list=[] #global list variable
#data input udf for user
def input_data():
    """This Function For User Input As 1d and 2d array"""
    global data_list#global list variable use
    data_list=[]
    print("Choices For Data Input:")
    print("1.1D Array")
    print("2.2 Array")
    choice=int(input("Enter Data Choice:"))
    match choice:
        case 1:
            user_data=input("Enter Data For 1D Array (Separated By Spaces) like 1 2 3 ...")
            data_list.append([int(x) for x in user_data.strip().split()])
            print(data_list)
        case 2:
           
           row=int(input("Enter Number Of Row For 2D Array:"))
           col=int(input("Enter Number Of Columns For 2D Array:"))
           for i in range(row):
               row_data=[]
               print(f"Enete Data For Row{i+1}:")
               for j in range(col):
                   value=int(input(f"Enter Data For Column{j+1}:"))
                   row_data.append(value)
               data_list.append(row_data)
     
           
                   
        case _:
            return 0
#data summary udf
def data_summary():
    """This Function Show Data Summary"""
    if(data_list==[]):
        print("No Any Data Found")
        return 0
    else:
        print("\nData Summary:")
        total_elements=sum(len(row) for row in data_list)
        items=[item for row in data_list for item in row]
        minimum_value=min(items)
        maximum_value=max(items)
        sum_of_all=sum(items)

        print(f"-Total Elements:{total_elements}")
        print(f"-Minimum Value:{minimum_value}")
        print(f"-Maximum Value:{maximum_value}")
        print(f"-Sum Of All Values:{sum_of_all}")
        print(f"-Average Value:{sum_of_all/total_elements}")
#factorial number calculate
def factorial(n=1):
    """This Function Is Calculate Factorial Deafault is 1"""
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
#filter data
threshold = lambda v=0: sorted([item for row in data_list for item in row if item >= v])

#sort data ascending and descending order
def sorting():
    """This Function For Sorting Data In Ascending And Descending Order"""
    print("1.Ascending")
    print("2.Descending")
    user_input=int(input("Enter Your Choice For Sorting:"))
    if data_list==[]:
        print("No Data Found Is Empty")
        return 0
    match user_input:
        case 1:
             for i in data_list:
                 i.sort()
             data_list.sort()
             print("Sorted Data In Ascending Orderd:")
             for i in data_list:
                print(i)

        case 2:
            for i in data_list:
                i.sort(reverse=True)
            data_list.sort(reverse=True)
            print("Sorted Data In Descending Orderd:")
            for i in data_list:
                print(i)
        case _:
            print("Invalid Command")
def data_statstics():
        """This Function For Data Statstics They Show\nAll  Data Statstics Of On User Data"""
        if(data_list!=[]):
            total_elements=sum(len(row) for row in data_list)
            items=[item for row in data_list for item in row]
            minimum_value=min(items)
            maximum_value=max(items)
            sum_of_all=sum(items)
            return total_elements,minimum_value,minimum_value,sum_of_all
        return None,None,None,None

#menu driven interface
while(True):
    print("\nMain Menu")
    print("1.Input Data")
    print("2.Display Data Summary(built-in functons)")
    print("3.Calculate Factorial")
    print("4.Filter Data By Threshold(Lambda Function)")
    print("5.Sort Data")
    print("6.Display Data Set Statstics(Return Multiple Values)")
    print("7.Exit Program")
    choice=int(input("Please Enter Your Choice:"))
    match choice:
        case 1:
            print(input_data.__doc__)
            input_data()
        case 2:
            print(data_summary.__doc__)
            data_summary()
        case 3:
            print(factorial.__doc__)
            num=int(input("Input a number to calculate its factorial:"))
            print(f"Factorial Of {num} is {factorial(num)}")
        case 4:
           
            value=int(input("Enter a threshold value to filter out data above this value:"))
            print(f"Filtered Data (values >= {value}):")
            print(threshold(value),sep=',')
        case 5:
            print(sorting.__doc__)
            sorting()
        case 6:
            print(data_statstics.__doc__)
            total_elements,minimum_value,maximum_value,sum_of_all=data_statstics()

            if total_elements is not None:
                print(f"-Minimum Value:{minimum_value}")
                print(f"-Maximum Value:{maximum_value}")
                print(f"-Sum Of All Values:{sum_of_all}")
                print(f"-Average Value:{sum_of_all/total_elements}")
            else:
                print("No Data Found")
            
        case 7:
            print("\nThanks For Using The Data Analyzer And Transformer Program. GoodBye!")
            break


    