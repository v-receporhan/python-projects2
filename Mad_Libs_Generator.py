madlib_story = f"""
Once upon a time, a programmer decided to build a  [adjective]  robot. 
This robot was special because it could [verb] all day long. 
One day, the robot saw a giant  [noun]  in the park. 
It bravely ran towards the [noun] and shouted, '[funny_word]!' 
The robot then picked up the [noun] and took it to [place]. 
Everyone agreed this was the most  [adjective_2]  robot in the world.
"""
print ("Welcome to the Mad Libs Generator!")
adjektive = input("Enter an adjective: For example.: silly, green, loud  ")
verb = input("Enter a verb: For example.: run, jump, dance  ")
noun = input("Enter a noun: For example.: dog, car, pizza  ")
funny_word = input("Enter a funny word: For example.: booger, giggle, poop  ")
place = input("Enter a place: For example.: park, school, beach  ")
adjektive_2 = input("Enter another adjective: For example.: amazing, tiny, colorful  ")

##replace eski değeri yeni değerle değiştirir 

madlib_story = madlib_story.replace("[adjective]", adjektive)
madlib_story = madlib_story.replace("[verb]", verb)
madlib_story = madlib_story.replace("[noun]", noun)
madlib_story = madlib_story.replace("[funny_word]", funny_word)
madlib_story = madlib_story.replace("[place]", place)
madlib_story = madlib_story.replace("[adjective_2]", adjektive_2)
print("\nHere is your Mad Libs story:",madlib_story)
