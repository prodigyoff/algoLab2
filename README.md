To launch doctests using console:  
1.Go to directory with main.py and managers  
2.Launch console from here  
3.Type in console: "python3 -m managers.bananas" (could be "py" or "python" depending on your python version)  
Brief algorithm description:  
1.Taking pile with largest bananas amount in it  
2.Eating bananas in piles untill there is nothing left  
3.Checking if this number of bananas per hour fits and decreasing it by 1 to find min number which fits  
4.When we got our number returning number+1 if it's not equal to 1, and if it is: returning number  
