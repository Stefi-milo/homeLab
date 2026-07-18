# here we use the module3

import module3

# once imported we can use it
print()
module3.greeting()

# modules are not protected from one another
module3.USEFUL_CONSTANT = 666
module3.greeting()
