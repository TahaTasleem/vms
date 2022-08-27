import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PreregComponent } from './prereg.component';

describe('PreregComponent', () => {
  let component: PreregComponent;
  let fixture: ComponentFixture<PreregComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PreregComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PreregComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
