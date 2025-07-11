import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Movie {
  id: number;
  title: string;
  desc: string;
  year: number;
}
@Injectable({
  providedIn: 'root'
})
export class Api {
  private readonly baseurl = "http://127.0.0.1:8000";
  private readonly httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
  
  constructor(private http:HttpClient) { }
      
  getAllMovies(): Observable<Movie[]> {
    return this.http.get<Movie[]>(this.baseurl + '/movie/', 
      {headers: this.httpHeaders}
    );
  }
}