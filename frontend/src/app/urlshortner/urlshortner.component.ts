import {Component, OnInit, ViewEncapsulation} from '@angular/core';
import {FormControl, Validators} from '@angular/forms';

@Component({
  selector: 'app-urlshortner',
  imports: [],
  templateUrl: './urlshortner.component.html',
  styleUrl: './urlshortner.component.css',
  encapsulation: ViewEncapsulation.None
})
export class URLShortnerComponent implements OnInit {
  urlControl: FormControl = new FormControl('', [
    Validators.required,
    Validators.pattern('https?://.+')
  ]);
  shortenUrl() {

  }
  ngOnInit(){

  }
}
