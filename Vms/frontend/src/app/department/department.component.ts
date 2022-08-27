import { Component, Input, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';
@Component({
  selector: 'app-department',
  templateUrl: './department.component.html',
  styleUrls: ['./department.component.css']
})
export class DepartmentComponent implements OnInit {

  constructor(private service:SharedService) { }
  // @Input() dep:any;
  // id:Int32List
  // // name:string;
  // item:any;
  id:number=0;
  name:string="";
  organization_name:string="";
  purpose:string="";
  cnic:string="";
  contact_no:string="";
  checkin_time:Date=new Date();
  checkout_time:Date=new Date();
  gender:string="";
  // emp_name:string="";
  employee_id:number=0;
  example:number=0;
  example2:string="";
  example3:string="";


  EmployeeList:any=[];
  VisitorList:any=[];
  visitorIdFilter:number=0;
  visitorNameFilter:string="";
  visitorListWithoutfilter:any=[];
  // dep:any;
  // ModalTitle:string;
  // ActivateAddEditDepComp:boolean=false;
  ngOnInit(): void {
    this.refreshDepList();
   }

  refreshDepList(){
    this.service.getEmpfromview().subscribe(data=>{
      this.VisitorList=data;
    })
  }
  
  
  deleteClick(item:any){
    if(confirm('Are you sure??')){
      this.service.deleteVisitor(item.id).subscribe(data=>{
        alert(data.toString());
        this.refreshDepList();
      })
    }
  }
  Sort(event:any){
    if(event.target.value==1){
      this.service.getSortAscVisitorList().subscribe(data=>{
        this.VisitorList=data;
      })
    }
    else if(event.target.value==2){
      this.service.getSortDescVisitorList().subscribe(data=>{
        this.VisitorList=data;
      })
    }
  }
  SortStatus(event:any){
      this.service.sortvisitorstatus(event.target.value).subscribe(data=>{
        this.VisitorList=data;
      })
  }

  SearchById(){
    // console.log(this.example);
    this.service.getVisitorFromId(this.example).subscribe(data=>{
      this.VisitorList=[data];
    });    
  }
  SearchByName(){
    this.service.getEmpNamefromVisitor(this.example3).subscribe(data=>{
      this.VisitorList=data;
    });
  }

}
