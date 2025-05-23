import { ComponentFixture, TestBed } from '@angular/core/testing';

import { URLShortnerComponent } from './urlshortner.component';

describe('URLShortnerComponent', () => {
  let component: URLShortnerComponent;
  let fixture: ComponentFixture<URLShortnerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [URLShortnerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(URLShortnerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
