import { Component, computed, inject } from '@angular/core';
import { Router } from '@angular/router';
import { QuizService } from '../../services/quiz.service';
import { MatCardModule } from '@angular/material/card';
import { MatRadioModule } from '@angular/material/radio';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule } from '@angular/forms'; // Necesario para ngModel

@Component({
  selector: 'app-question',
  standalone: true,
  imports: [MatCardModule, MatRadioModule, MatButtonModule, FormsModule],
  templateUrl: './question.html',
  styleUrl: './question.css'
})
export class Question {
  quizService = inject(QuizService);
  router = inject(Router);

  // Señal para obtener la pregunta actual
  currentQuestion = computed(() => {
    return this.quizService.questions()[this.quizService.currentQuestionIndex()];
  });

  selectedOption: string | null = null;
  
  // Señal para saber si es la última pregunta
  isLastQuestion = computed(() => {
    return this.quizService.currentQuestionIndex() === this.quizService.questions().length - 1;
  });

  submitAnswer() {
    if (this.selectedOption) {
      this.quizService.answer(this.quizService.currentQuestionIndex(), this.selectedOption);
      this.selectedOption = null; // Reinicia la selección
      
      if(this.isLastQuestion()){
        this.router.navigate(['/results']);
      } 
      else {
        this.quizService.nextQuestion();
      }
    }
  }
}
