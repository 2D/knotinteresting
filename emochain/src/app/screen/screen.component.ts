import { Component, OnInit } from '@angular/core';
import { Screen } from '../screen';

@Component({
  selector: 'app-screen',
  templateUrl: './screen.component.html',
  styleUrls: ['./screen.component.css']
})
export class ScreenComponent implements OnInit {

  screen: Screen = {
    id: 1,
    name: 'Page 1'
  };

  constructor() { }

  ngOnInit() {
  }

}
