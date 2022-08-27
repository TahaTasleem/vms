import { Component, OnInit,Input } from '@angular/core';
import { SharedService } from '../shared.service';


@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class reportsComponent implements OnInit {

  searchText:any;
constructor(private service:SharedService) { }
  
  id:number=0;
  name:string="";
  organization_name:string="";
  purpose:string="";
  cnic:string="";
  contact_no:string="";
  checkin_time:Date=new Date();
  checkout_time:Date=new Date();
  gender:string="";
  employee_id:number=0;
  status:string='';
  countCheckIn:any=0;
  countCheckOut:any=0;
  countScheduled:any=0;
  listcheckin:any=[];
  listcheckout:any=[];
  listschedule:any=[];


  ngOnInit(): void {
    // console.log(this.router.snapshot.params['val'])
    this.CountStatus();
    this.refreshDepList();
   }

   refreshDepList(){
    this.service.getVisitorFromStatus('Check In').subscribe(data=>{
      this.listcheckin=data;
      console.log(data)
    })
    this.service.getVisitorFromStatus('Check Out').subscribe(data=>{
      this.listcheckout=data;
    })
    this.service.getVisitorFromStatus('Scheduled').subscribe(data=>{
      this.listschedule=data;
    })
  } 

  CountStatus()
  {
    this.service.CountVisitorStatus('Check In').subscribe(data=>{
      this.countCheckIn=data;
      // console.log(data);
    })
    this.service.CountVisitorStatus('Check Out').subscribe(data=>{
      this.countCheckOut=data;
    })
    this.service.CountVisitorStatus('Scheduled').subscribe(data=>{
      this.countScheduled=data;
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

}
