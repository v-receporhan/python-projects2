import random

questions = [
    "what is the capital of France?",
      "what is 2 + 2?", "what is the capital of Germany?", 
      "what is 3 * 5?",
        "what is the capital of Italy?"]
# soru sallıyorum


#sample rastgele karıştırma seçme

answers = [""
"Paris",
 "4",
   "Berlin", 
   "15", 
   "Rome"]

### zip iki listeyi eşleştiriyor

qa_pair = list(zip(questions, answers))
random.shuffle(qa_pair)
i = 0
while i < len(qa_pair):
    qa_pair[i] = list(qa_pair[i])
    i += 1
score = 0
for q,a in qa_pair:
    user_answer = input(q + " ")
    if user_answer.lower() == a.lower():
      print("Correct!")
      score += 1
    else:
        print("Wrong! The correct answer is:", a)
        score -= 1
if i < 0 or i >= len(qa_pair):
   print("Your final score is:", score)
