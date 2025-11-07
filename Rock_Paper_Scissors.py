import random

def run_rock_paper_scissors():
    """Taş, Kağıt, Makas oyununu sürekli oynatır."""
    
    OPTIONS = ["rock", "paper", "scissors"]
    
    print("--- Welcome to Rock, Paper, Scissors Game ---")
    
    while True:
        # 1. Bilgisayarın rastgele seçimini yap
        computer_choice = random.choice(OPTIONS)
        
        # 2. Kullanıcıdan girdiyi al ve hemen küçük harfe çevir (Hata 3 düzeltildi)
        player_input = input("\nChoose (Rock, Paper, or Scissors) or type 'exit' to quit: ").lower()

        # 3. Çıkış kontrolü
        if player_input == 'exit':
            print("Thanks for playing! Goodbye.")
            break 
            
        # 4. Geçersiz girdi kontrolü
        # Kontrol, OPTIONS listesi doğru olduğu için artık düzgün çalışacak.
        if player_input not in OPTIONS:
            print(" Invalid choice! Please enter Rock, Paper, or Scissors.")
            continue
            
        # Seçimleri ekrana yazdır (Capitalize ile estetik düzeltme)
        print(f"\nYou chose: {player_input.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        print("--- Result ---")

        # 5. Mantık Kontrolü
        
        # Beraberlik Kontrolü
        if computer_choice == player_input:
            print("It's a tie! Draw game.")

        # Kazanma 
        elif (player_input == "rock" and computer_choice == "scissors") or \
             (player_input == "paper" and computer_choice == "rock") or \
             (player_input == "scissors" and computer_choice == "paper"):
            
            print("You win!")

        # Kaybetme
        else:
            print("Computer wins!")

# Fonksiyonu başlat 
run_rock_paper_scissors()