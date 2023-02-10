#Implementation of Simplified Unify Algorithm for Unification of Sentences with Predicate Logic
# created by 190104140_Ashiq at 2023-01-29 09:50.
# github.com/luqisha

# Sample Input 1:
# P1("Km", x, y)
# P1(z, u, F1(z))
# Sample Input 2:
# P1(f1, "now", x) 
# P1("any", "now", f1)  

theta = list()

def is_function(term):
    if("(" in term):
        function_symbol = term.split("(")[0]
        if(function_symbol.isalnum() and term[-1] == ")"):
            return True
        else:
            return False
    else:
        return False
        
def is_variable(term):
    if(term[0] != '"' and is_function(term)==False): 
        return True
    else:
        return False

def substitute(terms, prev, new):
    for j in range(len(terms)):
        if(is_function(terms[j])):
            terms[j] = terms[j].replace(prev, new)
        elif(terms[j] == prev):
            terms[j] = new
    return terms;

def unify(terms1, terms2):
    step = 0
    print("\nStep", step, ": ", end=" ")
    print("Theta = ", theta)

    while(terms1 != terms2):
        i = 0
        while(i < len(terms1)):
            if(terms1[i] != terms2[i]):
                if(is_variable(terms1[i])):
                    theta.append(terms1[i] + "/" + terms2[i])
                    #substitute terms of sentance 1 that is the same as terms1[i], with the value of terms2[i]
                    terms1 = substitute(terms1, terms1[i], terms2[i])
                elif(is_variable(terms2[i])):
                    theta.append(terms2[i] + "/" + terms1[i])
                    #substitute terms of sentance 2 that is the same as terms2[i], with the value of terms1[i]
                    terms2 = substitute(terms2, terms2[i], terms1[i])
                elif((is_function(terms2[i]) and terms1[i] in terms2[i]) or 
                     (is_function(terms1[i]) and terms2[i] in terms1[i])):
                        #Stop unifying as a term contains the the other variable
                        return False
                else:
                    theta.append(terms1[i] + "/" + terms2[i])
                    terms1 = substitute(terms1, terms1[i], terms2[i])
                step+=1
                print("Step " + str(step) + ": ", end=" ")
                print("Theta =", theta)
            i+=1
    return True


sentence1 = input("Sentence 1 : ").replace(" ", "")
sentence2 = input("Sentence 2 : ").replace(" ", "")

predicate1 = sentence1.split("(")[0]
predicate2 = sentence2.split("(")[0]

terms1 = sentence1.replace(predicate1, "")
terms1 = terms1[1: len(terms1)-1].split(",")

terms2 = sentence2.replace(predicate2, "")
terms2 = terms2[1: len(terms2)-1].split(",")

if (predicate1 != predicate2):
    print("Predicates don't match, Not unifiable!")
elif (len(terms1) != len(terms2)):
    print("Number of terms don't match, Not unifiable!")
else:
    if(unify(terms1, terms2) == False):
        print("Not unifiable!")
    else:
        print("\nMost General Unifier: ", theta)
             


