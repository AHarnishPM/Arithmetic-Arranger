def arithmetic_arranger(problems, tf=False):
  L1 = ""
  L2 = ""
  L3 = ""
  L4 = ""
  x = "    "

  if len(problems) > 5:
    return "Error: Too many problems."
    
  for i in problems:
    #split problem by spaces
    t = i.split()

    if len(t[0]) > 4 or len(t[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    if not t[0].isnumeric() or not t[2].isnumeric():
      return "Error: Numbers must only contain digits."

    if t[1] != "+" and t[1] != "-":
      return "Error: Operator must be \'+\' or \'-\'."
    
    #set width (iteration) to length of longest number +2 (operator)
    width = max(len(t[0]), len(t[2])) + 2
    
    #Add first number to line 1 list with spacing
    spc = width - len(t[0])
    L1 += " "*spc + t[0] + x

    #Add operator, spaces, second number with correct spacing to line 2 list
    spc = width - 1 - len(t[2])
    L2 += t[1] + " "*spc + t[2] + x
    
    #Add "-" * width to third line
    L3 += '-'*width + x

  arranged_problems = L1.rstrip() + '\n' + L2.rstrip() + '\n' + L3.rstrip()

  if tf != False:
    for i in problems:
      
      #split problem by spaces
      t = i.split()
      
      #find width again
      width = max(len(t[0]), len(t[2])) + 2
      
      #solve problem
      if t[1] == '+':
        A = int(t[0]) + int(t[2])
      elif t[1] == '-':
        A = int(t[0]) - int(t[2])
        
      #add solution to line 4 with spacing
      spc = width-len(str(A))
      L4 += " "*spc + str(A) + x
    arranged_problems += '\n' + L4.rstrip()


  return arranged_problems
