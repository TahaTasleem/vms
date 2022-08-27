import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { EmployeeComponent } from './employee/employee.component';
import { DepartmentComponent } from './department/department.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { Form2Component } from './form2/form2.component';
import { PreregComponent } from './prereg/prereg.component';
import { GroupformComponent } from './groupform/groupform.component';
import { reportsComponent } from './reports/reports.component';

const routes: Routes = [
{path:'visitorlist',component:DepartmentComponent},
{path:'newappointment',component:GroupformComponent},
{path:'newappointments/:id',component:EmployeeComponent},
{path:'empappointments/:id',component:Form2Component},
{path:'',component:DashboardComponent},
{path:'dashboard',component:DashboardComponent},
{path:'preregistration',component:PreregComponent},
{path:'reports',component:reportsComponent},
// {path:'logout',component:GroupformComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
