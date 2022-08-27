import { ComponentFixture, TestBed } from '@angular/core/testing';

import { reportsComponent } from './reports.component';

describe('reportsComponent', () => {
  let component: reportsComponent;
  let fixture: ComponentFixture<reportsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ reportsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(reportsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
