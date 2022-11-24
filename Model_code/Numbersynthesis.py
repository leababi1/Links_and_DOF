# L - 3 - M = 1T + 2Q + 3P + 4H + ...
# L = B + T + Q + P + H + ...
import math
links = [[]]
type = 0
outputString = ""
finalString = ""
def calculate(counter, l, l3m, coefficient):
    if (l3m >= 0) and (coefficient >= 1):
        available = l3m / coefficient
        if (available >= 1) and (coefficient != 1):
            integer = math.floor(available)
            links[counter].append(integer)
            #print(links)
            newlink = links[counter].copy()
            calculate(counter, l, l3m - coefficient * integer, coefficient - 1)
            for i in range(integer-1, -1, -1):
                links.append(newlink.copy())
                #print(links)
                links[-1][-1] = i
                #print(links)
                #testing
                #counter += 1
                counter1 = len(links) - 1
                calculate(counter1, l, l3m - coefficient*i, coefficient - 1)
        else:
            if (coefficient == 1) and (available >= 1):
                integer = math.floor(available)
                links[counter].append(integer)
                #print(links)
                calculate(counter, l, l3m - coefficient * integer, coefficient - 1)
            else:
                links[counter].append(0)
                #print(links)
                calculate(counter, l, l3m, coefficient - 1)
    else:
        while len(links[counter]) != (type - 2):
            links[counter].append(0)
        for integers in links[counter]:
            l = l - integers
        links[counter].append(l)
        #print(links)


def numberSynthesis(M, L, Type):
    global finalString
    finalString = ""
    global outputString
    outputString = ""
    global type
    type = Type
    if (M % 2) == 0:
        L1 = 1
    else:
        L1 = 0
    while L1 < (3 + M):
        L1 = L1 + 2

    while L1 <= L:
        L3M = L1 - 3 - M
        calculate(0, L1, L3M, Type - 2)
        global links
        for link in links:
            link.reverse()

        outputString = outputString + ("L = %s:" % L1) + " [ | "
        for link in links:
            outputString = outputString + "["
            for number in range(0, len(link)-1):
                outputString = outputString + str(link[number]) + ", "
            outputString = outputString + str(link[-1]) + "] | "
        outputString = outputString + "]" + "\n"

        #print("L = %s" % L1, end=": "), print(links)
        #print(outputString)

        finalString = finalString + outputString + "\n"
        outputString = ""
        links = [[]]
        L1 = L1 + 2
    return finalString

#print(numberSynthesis(2, 9, 6))
