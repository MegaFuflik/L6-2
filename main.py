num=9696
def rot(num1):
    if num1>9000: 
        num1=num1-9000
        if num1>900: 
            num1=num1-900
            if num1>90: 
                num1=num1-90
                if num1==9: 
                    return(9999)
                else:
                    return(9996)                   
            else:
                num1=num1-60
                if num1==9: 
                    return(9996)
                else:
                    return(9966)
        else:
            num1=num1-600
            if num1>90: 
                num1=num1-90
                if num1==9: 
                    return(9996)
                else:
                    return(9966)
            else:
                num1=num1-60
                if num1==9: 
                    return(9966)
                else:
                    return(9666)
    else: 
        num1=num1-6000
        if num1>900: 
            num1=num1-900
            if num1>90: 
                num1=num1-90
                if num1==9: 
                    return(9996)
                else:
                    return(9696)
            else:
                num1=num1-60
                if num1==9: 
                    return(9669)
                else:
                    return(9666)
        else:
            num1=num1-600
            if num1>90: 
                num1=num1-90
                if num1==9: 
                    return(9696)
                else:
                    return(6696)
            else:
                num1=num1-60
                if num1==9: 
                    return (9666)
                else:
                    return  (6666) 
rot(num)           

if __name__ == "__main__":    
    print("example 1", rot(9669))
    print("example 2", rot(9996))
    print("example 3", rot(9999))