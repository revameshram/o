p_spam=float(input("enter p(spam) by your observation : "))
p_free_spam=float(input("enter p(free|spam) by your observation : "))
p_free_ham=float(input("enter p(free|ham) : "))

p_ham=1-p_spam

#to find p(spam|free)

#p(spam|free)=(p(free|spam)*p(spam))/p(free)

#for p(free):
p_free=p_free_ham*p_ham+p_free_spam*p_spam

p_spam_free=(p_free_spam*p_spam)/p_free

print(p_spam_free)