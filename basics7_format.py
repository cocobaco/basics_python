import random
import numpy as np

def relu(input):
    # Calculate the value for the output of the relu function: output
    output = max(input, 0)
    return(output)

def myformat(x):
    #return ('%.2f' % x).rstrip('0').rstrip('.')
    return ('%3.2g' % x)
    #return ('{0:.2f}' % x)

if __name__ == '__main__':    
    myrand1 = random.random()*100
    print('%.5f' % myrand1)
    print(f'{myrand1:.2f}')
    print(f'{myrand1:.1f}')
    
    yrinput = float(input("enter a float: "))
    #print(round(yrinput,2))
    print(myformat(yrinput))
    print(relu(yrinput))
    print('${:,.2f}'.format(yrinput))
    print('${:20,.4f}'.format(yrinput))
    print('${:03,.1f}'.format(yrinput))
    
    ## -------- numpy -------------
    print('numpy-----')
    np_ran=np.random.random(10)*100
    print(np_ran)
    np.set_printoptions(precision=2,suppress=True)
    print(np_ran)