# To solve this problem, we will use Burnside's Lemma.
# Which we will call BL from now on. 
# For code, just skip all this commentary and scroll down. 
# This was a monstrously difficult problem so I have to break it down 
# piece by piece as well as explain some concepts to myself (and possibly
# to anyone reading this) piecemeal.

# For a quick intro, first watch this following 6 videos.
# https://www.youtube.com/watch?v=D0d9bYZ_qDY

# https://www.youtube.com/watch?v=VOrVMQjQpGg
# https://www.youtube.com/watch?v=QtZ9H5U0SwM
# https://www.youtube.com/watch?v=pheASxiQk2I

# https://www.youtube.com/watch?v=wvofB5tZz3Y
# https://www.youtube.com/watch?v=Tkz8QGPHxdA

# It's also important to learn about Polya's Theorem (which we will
# call PT from now on) because it will introduce the concept of
# the cycle notation, cycle index, and counting cycles.
# Both BL and PT are basically the same thing but with more concepts
# introduced in PT. If BL is the base game, PT is the $29.99 DLC. 

# This problem is extremely difficult for me so I will try to explain
# what I can but I've the mastery over this like a man treading water
# barely able to stay afloat so I do appreciate your patience.


# Burnside's Lemma is simply defined as 
# "The number of orbits is equal to Sum(X) / |G| "
# Orbit = Unique configuration by grouping (what we're trying to find)
# |G| = The size or length of all symmetries or group actions. If G was an array,
# this would be like G.length()
# X = A function for each g in G (there's a little icon that looks like an E 
# 	but bent to a c shape to represent this but I'll just say "for each x
# 	in a set that contains all x's")

# [Terminology Clarification] Color. Each configuration of whatever thing we're looking at 
# (the order of beads in necklace, chess boards rotations, star configurations) is called 
# a color. When you spin a chess board 90 degrees or change how the beads in a necklace
# are arranged, you're now looking at a new "color".

# [Terminology Clarification] Group. In Burnside's Lemma, a group
# does not mean exactly what it means in English. In BL, when we say group, we 
# are specifically referring to G which is a set of all symmetries or actions. 
# Each symmetry is sort of like a verb. So elements of G are "actions" that can
# be performed on whatever color we're looking at whether it's rotating it, flipping it
# vertically, or swapping some beads around in a necklace. 
# Symmetries and group elements refer to the same thing: g (which is an element in set G) 

# When g in G acts upon something, we call it a "group action". So the group action
# of a 90 degree reflection clockwise on the chess board we're looking at creates
# a new "color" for the chess board.

# So what is X in BL? X is a FOR loop (or summation in math terms) that loops through each 
# element of G and does something. 
# Fundamentally what we're doing is going through every single possible color, compare it to every
# single g in G, and recording which g is a "stabilizer" for the color we're looking at. 
# We then add up the total number of color/stabilizer pairs we find and divide that by the total
# number of elements in G. 

# All together and BL basically states that the number of distinct orbits is equal to:
# "The average number of colors stabilized by each group element".

# [Terminology Clarification] Stabilizer. A stabilizer is a g in G that when it acts on a color,
# an identity color (literally the same color) is created. So this is just another label for a 
# g in G but it's special because when you apply this g to say, a color labeled X, you get X.
# This can be defined as: g * x = x
# We use the * symbol here which means "to act upon". So g is "acting upon" x but the product of
# this act is just x, aka the identity. 

# [Terminology Clarification] Conjugacy. We will use this term later but conjugacy is the
# term used to define this sort of equivalence created by a stabilizer. Earlier, we defined a 
# stabilizer as a symmetry or group element g if g acting on color X produces X. If stabilizer
# refers to the group element here, conjugacy refers to the color. 
# For g in G, if:
# g * a = b
# and 
# g * b = a
# Then we can say that a is a "conjugate" of b and vice versa. 
# [Great explanation here](https://www.youtube.com/watch?v=o5xR8Vu7oH8)

# Back to the problem at hand, the devil is always in the details and in this case,
# the Dark Souls boss we're facing is the X in X/G. I know earlier we said that X is simply
# finding all colors that are stabilized by each g in G but as the number of colors increase, 
# it becomes impractical to count every single color so we have to optimize for this by thinking 
# "What parts of this thing actually matters when we transform it via g?" Which part of it 
# contributes to the fact that g is acting as a stabilizer?

# To expand on X a bit, in the classical chess board example of BL, X is
# Orbits = (s**Z)/|G| where s is the number of states and Z is the number of
# squares that matter. For example, on a chess board, s would be 2 because each square can only 
# be two colors. If there were 3 colors, s would be 3, and so on and so forth. 
# Z in this case would be the "squares on the chess board that matter" when you apply g. 
# For example, when flipping a board horizontally, only half the squares matter because they must
# identical. Whatever half of the board looks like, the other half must be a mirror image of 
# in order for the product of the flip to be a conjugate of the pre-flip:
# (vertical flip) * chess_board_a = chess_board_b
# where chess_board_a == chess_board_b

# In our exact case, it gets way more complex because our symmetries or group actions are NOT
# simple rotations or reflections; they are swapping out columns and rows for each other any
# number of times. So lets start breaking down exactly what we're going to do:

# Orbits = (1/|G|) * for g in G: sum(something with g)

# So what's len(G)? It is simply w! * h!. This is because w!h! will account for literally every
# single permutation of row swap and column swap. If we just looked at height swaps, it would be h!
# and same for rows and w! so when we add them together, we get everything!

# Next step: what is g? It will be used in the sum(). Earlier we figured out that |G| was w!h! but
# what is each individual g? Well, as it turns out, each height and row "group element action" is 
# actually an "integer partition" (https://en.wikipedia.org/wiki/Partition_(number_theory)).
# There is actually an entire reason for this and it goes over my head but it has to do with taking
# cycle notation of g in G of what's being swapped around assuming that the larger cycles are written
# first in the cycle notation. 

# We will do a nested for loop where we do:

# sum = 0
# for each partition of h
# 	for each partition of w
# 		sum += (do something)

# orbit = sum / |G|

# Like before in other BL, we will do s**something for each g. That "something" will be to 
# use a nested for loop and sum together the GCD of every single element of each integer
# partition in partition of h and partition of w.

# sum = 0
# for each element (i) in partition of h
# 	for each element (j) in partition of w
# 		sum += gcd(i,j)

# s**sum

# To see why we need to take the greatest common divisor (GCD) during BL, 
# [look here](https://mathoverflow.net/questions/244913/simple-proof-for-sum-i-1n-a-gcdi-n-is-divisible-by-n)

# Recap:
# Orbits = sum( for g in G, s**Z ) / len(G)

# We now know what g, G, s, and Z is but we are still missing the conjugate classes of gh and gw.
# Orbits = sum( for g in G, (s**Z)*(cl(gh)*cl(gw)) ) / len(G)

# [Terminology Clarification] Conjugate classes. 
# Conjugacy of g's in G is an equivalence relation. Equivalence relations give rise to equivalence
# classes. G can be partitioned into equivalence classes.
# Basically, if two elements in G are conjugates, they are in a conjugate class. Orbits for G.
# This is weird because colors are nouns while g's are "verbs". So how can two verbs be equivalent?
# Because sometimes, two verbs acting on a noun does the same thing. Flipping something vertically and
# rotating it 180 degrees does the same thing to a chess board so in this case, the flip and the rotation
# are in the same conjugate class. 
# Class number of G is the number of distinct nonequivalent conjugacy classes. They're basically
# "orbit equivalents" but for G.
# To find the number of elements in a conjugacy class for an integer partition:
# https://groupprops.subwiki.org/wiki/Conjugacy_class_size_formula_in_symmetric_group
# To break it down:
# let n = width or height or whatever
# let p = integerPartition(n)
# conjugacyClassSize = n! / product( j**a * a! )
# where j = each number in the partition 
# where a = how many time that number shows up
# So we will need to transform this integer partition from (1,1,2)
# into something like
# { 1: 2,
#   2: 1 }
# Because we don't want to loop through 1 twice. This is sort of like a set but with dict aspect. 
# So do this:
# https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list

# -----------The Code-----------

# Let's build this: # Orbits = sum( for g in G, (s**Z)*(cl(gh)*cl(gw)) ) / len(G)

# Beginning with the integer partition builder. I know there are recursive ways to do this but I wanted to
# do it this way. Could be optimized though. This will create an empty list and append them like this
# if n=5:
# [5] 
# [1, 4]
# [2, 3]
# [1, 1, 3]
# [1, 2, 2]
# [1, 1, 1, 2]
# [1, 1, 1, 1, 1]
import copy

def partitions(n):
  if n == 0:
    return []
  
  # Start off the first one which is just the identity
  the_partitions = [[n]]

  # The last partition should be all 1's with length equal to n
  while len(the_partitions[-1])!=n:
    
    the_last_partition = copy.deepcopy(the_partitions[-1])

    # Let's loop through each number in the partition.
    for i, v in enumerate(the_last_partition):

      # Keep looping until we get to our first non "1"
      # This could be optimized. Maybe just return the index of the first
      # value that's not 1.
      if v == 1:
        continue
      else:
        # For the first non 1 we get to, subtract that number by 1
        new_v = v - 1
        # if that would change the number that we're about to subtract from into a 1,
        # OR there are no previous elements because we're on index 0
        # extend the array with a 1 instead from the front (the 0th position)
        if new_v == 1 or i == 0:
          the_last_partition[i] = new_v
          the_last_partition.insert(0, 1)
          the_partitions.append(the_last_partition)
          break
        else:
          # if v-1 != 1 and we're not at index 0,
          # subtract one from the current element and add it to the previous element.
          the_last_partition[i] = new_v
          the_last_partition[i-1] += 1
          the_partitions.append(the_last_partition)
          break

  return the_partitions


#Orbits = sum( for g in G, (s**Z)*(cl(gh)*cl(gw)) ) / len(G)


# -----------Ending Commentary-----------
# I find it ironic that in the first level of the Foobar challenge, there was a question about
# finding prime numbers where I simply used the Sieve of Eratosthenes (my own implementation was
# too slow). I remarked that I'm was not a mathematician and doubt I would have invented such
# an algorithm on my own in the limited time given to solve the problem. Come level 5 and
# I'm face with a problem that is purely math. All you need from CS courses to solve this
# are for loops and arrays; the rest are all combinatorics. 

# This challenge was extremely difficult because it had very little to do with coding. The concepts
# were unfamiliar to me and when researching group theory, every article and paper were filled with
# jargon that linked to something else. It was like an exercise of a human driven depth first search
# where each unknown word would lead to another and you had to explore every node of knowledge
# before coming back to a previously walked node that was now digestible. 

# Very fun, one of the best challenges of my life.

# Thanks Google.
