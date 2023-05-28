
def arithmetic_arranger(problem, answer = False):
  #define list of problems
  problemList = []
  #strip spaces from problems
  for x in problem:
    strippedproblems = x.replace(" ", "")
    problemList.append(strippedproblems)
  #define lists
  leftoperands = []
  operators = []
  rightoperands = []
  dashes = []
  lengths = []
  formattedleftoperands = []
  formattedrightoperands = []
  #check if user submitted too many problems
  if len(problemList) > 5:
    err_toomanyproblems = "Error: Too many problems."
    return err_toomanyproblems
  #check if user input a multiplication or division problem 
  for x in problemList:
    if '/' in x:
      err_wrongoperator = "Error: Operator must be '+' or '-'."
      return err_wrongoperator
    if '*' in x:
      err_wrongoperator = "Error: Operator must be '+' or '-'."
      return err_wrongoperator
  #Check if operator is present, is so find it's position
  for x in problemList:
    if '+' in x:
      operatorposition = x.find('+')
    elif '-' in x:
      operatorposition = x.find('-')
    else:
      err_nooperator = "At least one problem is missing an operator"
      return err_nooperator
  #Using operator position, find left operand and right operand  
    lengthOfProblem = len(x)
    leftoperand = x[:operatorposition]
    rightoperand = x[operatorposition+1:lengthOfProblem]
    operator = x[operatorposition]
  #check if operands are digits
    if leftoperand.isdigit() == False:
      err_isdigit = "Error: Numbers must only contain digits."
      return err_isdigit
    if rightoperand.isdigit() == False:
      err_isdigit = "Error: Numbers must only contain digits."
      return err_isdigit
  #check if length of operands is greater than 4
    if len(leftoperand) > 4:
      err_toomanydigits = "Error: Numbers cannot be more than four digits."
      return err_toomanydigits
    if len(rightoperand) > 4:
      err_toomanydigits = "Error: Numbers cannot be more than four digits."
      return err_toomanydigits
  #add values to their respective lists
    leftoperands.append(leftoperand)
    rightoperands.append(rightoperand)
    operators.append(operator)
  #check for larger operand in order to inform how many dashes should be present 
    if len(rightoperand) > len(leftoperand):
      numberOfDashes = len(rightoperand) + 2
    else:
      numberOfDashes = len(leftoperand) + 2
  #add dashes to their own list    
    if numberOfDashes == 6:
      dashes.append("------    ")
      lengths.append(6)
    if numberOfDashes == 5:
      dashes.append("-----    ")
      lengths.append(5)
    if numberOfDashes == 4:
      dashes.append("----    ")
      lengths.append(4)
    if numberOfDashes == 3:
      dashes.append("---    ")
      lengths.append(3)
  #right justify each operand depending on the lengths of the problems    
  for i in range(len(leftoperands)):
    formattedleftoperands.append(leftoperands[i].rjust(lengths[i]))
    formattedrightoperands.append(operators[i] + rightoperands[i].rjust(lengths[i] - 1))
  #print problems in vertical arrangement!
  finaldash = dashes[len(dashes)-1]
  strippedfinaldash = finaldash[0:len(finaldash)-4]
  dashes.pop()
  dashes.append(strippedfinaldash)
  formattedProblem =  '    '.join(formattedleftoperands) + "\n" + '    '.join(formattedrightoperands) + "\n" + ''.join(dashes)
  #if user wants answer to their problem, calculate answer
  if answer == True:
    answers = []
    formattedanswers = []
  #check if problem is addition or subtraction  
    for i in range(len(leftoperands)):
      if operators[i] == "+":
        answers.append(int(leftoperands[i]) + int(rightoperands[i]))
      else:
        answers.append(int(leftoperands[i]) - int(rightoperands[i]))
  #append right justified answers to list:formattedanswers      
    for i in range(len(leftoperands)):
      formattedanswers.append(str(answers[i]).rjust(lengths[i]))
    #print answers in vertical arrangement
    formattedProblem =  '    '.join(formattedleftoperands) + "\n" + '    '.join(formattedrightoperands) + "\n" + ''.join(dashes) + "\n" + '    '.join(formattedanswers)
  return formattedProblem

    
  







