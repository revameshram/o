
d=float(input("rarity of disease(in prob) : "))
a=float(input("accuracy of test(in prob) : "))
f=float(input("fasle positive rate(in prob) : "))

p_i=d   #probability of infection calculated from rarity
p_h=1-d  #prob of not infected ie. healthy
p_positive_i=a #probability of test positive given that infected (from accuracy)
p_negative_i=1-a #p(negative|infected)
p_positive_h=f #prob of positive test given that (healthy) not infected (from false positive rate)
p_negative_h=1-f  #p(negative|healthy)

#to find : p(i|positive): prob of person is infected if test is positive

#p(i|positive)={p(positive|i)*p(i)}/p(positive)   ..........bayes theorem

#for p(positive) using joint prob

p_positive=p_positive_h*p_h+p_positive_i*p_i

p_i_positive=(p_positive_i*p_i)/p_positive

print("prob that person is infected given that test is positive is : ",p_i_positive)

