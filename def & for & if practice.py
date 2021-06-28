def printcontent(name,score,be,adjective,number):
    for show in range(1,number):
       if score >= 60:
          print(show ,name + be + adjective)
       else:
          print(show , name + be + "not" + adjective)
printcontent("jack",50,"is","good",10)





