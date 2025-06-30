import { Injectable, signal, computed } from '@angular/core';

type GameStatus = 'playing' | 'won' | 'lost';

@Injectable({
  providedIn: 'root'
})
export class Hangman {
  private words = ['ANGULAR', 'TYPESCRIPT', 'COMPONENT', 'SERVICE', 'SIGNAL', 'DEVELOPER', 'SYSTEMS'];
  
  // *-- Banderas de ESTADO --+
  // La palabra que el jugador debe adivinar. Es privada.
  private secretWord = signal<string>('');
  // Las letras que el usuario ya ha intentado.
  public triedLetters = signal<string[]>([]);
  
  // +-- Banderas (REACTIVAS) --+
  // El número de errores se calcula solo cada vez que `triedLetters` cambia.
  public mistakesCount = computed(() => {
    const word = this.secretWord();
    return this.triedLetters().filter(letter => !word.includes(letter)).length;
  });
  
  // La palabra mostrada como por ej: 'PO_LO' se calcula sola.
  public displayWord = computed(() => {
    const word = this.secretWord();
    const letters = this.triedLetters();
    return word.split('').map(letter => (letters.includes(letter) ? letter : '_')).join(' ');
  });

  // Estado de juego autocalculado
  public gameStatus = computed<GameStatus>(() => {
    if (this.mistakesCount() >= 9) {
      return 'lost';
    }
    // Mensajde de ¡Ganaste (won)!, si ya no hay guiones vacíos
    if (!this.displayWord().includes('_')) {
      return 'won';
    }
    return 'playing';
  });

  // Expone la palabra secreta SOLO si el juego se ha perdido.
  public revealedWord = computed<string>(() => {
    if (this.gameStatus() === 'lost') {
      return this.secretWord();
    }
    return ''; // Devuelve una cadena vacía en cualquier otro caso.
  });

  constructor() {
    this.startNewGame();
  }

  // --- ACCIONES (MÉTODOS PÚBLICOS) ---
  public startNewGame() {
    // 1. Elegimos una palabra random
    const randomIndex = Math.floor(Math.random() * this.words.length);
    this.secretWord.set(this.words[randomIndex]);
    
    // 2. Reiniciamos intentos
    this.triedLetters.set([]);
  }

  public tryLetter(letter: string) {
    // Si el juego no ha terminado y la letra no ha sido intentada...
    if (this.gameStatus() === 'playing' && !this.triedLetters().includes(letter)) {
      // ...añadimos la letra a la lista de intentos.
      this.triedLetters.update(letters => [...letters, letter]);
    }
  }
}