cars =read.csv(file.choose())
MPG <- cars$MPG

sample(MPG)

a=subset(MPG,MPG>38)

show(a)
#ans = 33/81

b=subset(MPG,MPG<40)

show(b)
#ans = 57/81

c=subset(MPG,MPG>20 & MPG <50)

show(c)
#ans = 65/81
