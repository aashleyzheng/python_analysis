import tools    

#自訂function(內建的變數)，主執行區域
#自訂function，前面一定要有def main()
#程式由上而下執行不會去執行def main()
#使用的變數為區域變數
def main(): 
    height:int = int(input("請輸入身高公分"))
    weight:int = int(input("請輸入體重公斤"))
    #BMI = round(weight/pow(height/100,2),1)
    BMI:float = tools.get_bmi(weight,height)

    print(f"身高:{height}""cm")
    print(f"體重:{weight}""kg")
    print(f"BMI:{BMI}")
    status:str = tools.get_status(BMI) #BMI為引數值，真正的值
    print(f"狀態為:{status}")
    

#專案主要執行檔 => 名字就會叫做main
#全域變數
#if __name__ == '__main__': => 文件的敘述
if __name__ == '__main__':
    main() #呼叫 def main() 這個function